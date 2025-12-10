print("=========== BLOOD PRESSURE ANALYZER ===========")

systolic = int(input("Enter Systolic Pressure (mmHg): "))
diastolic = int(input("Enter Diastolic Pressure (mmHg): "))

if systolic < 90 or diastolic < 60:
    status = "Low Blood Pressure"
elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
    status = "Normal Blood Pressure"
elif 120 < systolic <= 139 or 80 < diastolic <= 89:
    status = "Pre-Hypertension"
else:
    status = "High Blood Pressure"

print("\n--------------- RESULT ----------------")
print(f"Systolic : {systolic} mmHg")
print(f"Diastolic: {diastolic} mmHg")
print("Condition:", status)
print("---------------------------------------")
