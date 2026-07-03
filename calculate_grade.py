def calculate_grade(scores):
    # ตรวจสอบก่อนว่าลิสต์ว่างหรือไม่ เพื่อป้องกันการหารด้วยศูนย์ (ZeroDivisionError)
    if not scores:
        return "No scores provided", 0

    total = 0 
    for score in scores: 
        total = total + score 

    average = total / len(scores) 

    # แก้ไขการย่อหน้า (Indentation) ให้ตรงกัน
    if average >= 80: 
        grade = "A" 
    elif average >= 70: 
        grade = "B" 
    elif average >= 60: 
        grade = "C" 
    elif average >= 50: 
        grade = "D" 
    else: 
        grade = "F" 

    return grade, average 

# ทดสอบการใช้งาน
scores = [85, 92, 78, 88, 95] 
grade, avg = calculate_grade(scores)
print(f"Average: {avg}, Grade: {grade}")
