import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF, XPos, YPos

# --------------------------
# Read CSV File
# --------------------------
df = pd.read_csv("students.csv", sep=',', engine='python', header=0)
df.columns = df.columns.str.strip()

# --------------------------
# Data Analysis
# --------------------------
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

highest = df["Average"].max()
lowest = df["Average"].min()
overall_average = df["Average"].mean()

top_student = df.loc[df["Average"].idxmax(), "Name"]

# --------------------------
# Create Bar Chart
# --------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.tight_layout()

chart_name = "average_marks.png"
plt.savefig(chart_name)
plt.close()

# --------------------------
# Generate PDF Report
# --------------------------
pdf = FPDF()

pdf.add_page()

pdf.set_font("Helvetica", "B", 18)
pdf.cell(0, 10, "Student Performance Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

pdf.ln(10)

pdf.set_font("Helvetica", size=12)

pdf.cell(0,10,f"Overall Average Marks : {overall_average:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0,10,f"Highest Average       : {highest:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0,10,f"Lowest Average        : {lowest:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0,10,f"Top Student           : {top_student}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(10)

pdf.set_font("Helvetica","B",12)

pdf.cell(45,10,"Name",1)
pdf.cell(35,10,"Math",1)
pdf.cell(35,10,"Science",1)
pdf.cell(35,10,"English",1)
pdf.cell(40,10,"Average",1)

pdf.ln()

pdf.set_font("Helvetica",size=12)

for _, row in df.iterrows():
    pdf.cell(45,10,row["Name"],1)
    pdf.cell(35,10,str(row["Maths"]),1)
    pdf.cell(35,10,str(row["Science"]),1)
    pdf.cell(35,10,str(row["English"]),1)
    pdf.cell(40,10,f"{row['Average']:.2f}",1)
    pdf.ln()

pdf.ln(10)

pdf.image(chart_name, x=20, w=170)

pdf.output("Student_Report.pdf")

print("PDF Report Generated Successfully!")