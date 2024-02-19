from main import StudentsInMLOps

obj = StudentsInMLOps()

def test_getTotalStrengthmodule():
    assert obj.getTotalStrength()==0

def test_getClassNamemodule():
    assert obj.getClassName()=="MLOps"

def test_enrollStudentsmodule():
    obj.enrollStudents("Hamza")
    assert obj.getTotalStrength()==1

def test_dropStudents():
    obj.dropStudents("Hamza")
    assert obj.getTotalStrength()==1
