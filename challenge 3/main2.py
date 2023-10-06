class Student:
  def __init(self,name,roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa 
def sort_students(student_list):
  sorted_students = sorted(student_list,key = lambda student: student.cgpa,reverse=true)
  return sorted_students
  students = [
  student("mathu","1234","7.8")
  student("oviya","0897","6.9")
  student("rudhra","7654","9.0")
  ]
  sorted_students = sort_students(students)
  for students in sorted_students:
    print("Name: {}, Roll number: {}, CGPA: {}".format(student.name,
      student.roll_number, student.cgpa))