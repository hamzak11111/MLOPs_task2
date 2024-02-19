class StudentsInMLOps():

    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"
        self.enrolled_students=[]

    def enrollStudents(self,student):
        self.enrolled_students.append(student)
        self.total_strength+=1

    def dropStudents(self,student):
        self.enrolled_students.remove(student)

    def getTotalStrength(self):
        return self.total_strength
    
    def getClassName(self):
        return self.class_name
