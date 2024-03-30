from fastapi import FastAPI
import uvicorn 

app = FastAPI()


students=[{
    "id":1,
    "Name":"sajjad",
    "age":30,
    "grade":"A+"
},
{
    "id":2,
    "Name":"aqib",
    "age":20,
    "grade":"b+"
},{
    "id":3,
    "Name":"amir",
    "age":25,
    "grade":"c+"
},{
    "id":4,
    "Name":"babr",
    "age":23,
    "grade":"d+"
}]

@app.get("/students")
def getStudents():
    global students
    return students

@app.get("/singlestudent")
def getSingleStudent(studentid: int):
    global students
    for singleStudent in students:
        if singleStudent ["id"] == studentid:
            return singleStudent 
    return {"message": "Student not found"}

@app.post("/addstudent")
def addStudent(id: int, Name: str, age: int, grade: str):
    global students
    new_student = {"id": id, "Name": Name, "age": age, "grade": grade}
    students.append(new_student)
    return students

@app.put("/updatestudent/{studentid}")
def putStudent(studentid: int, updated_student: dict):
    global students
    for student_update in students:
        if student_update["id"] == studentid:
            student_update.update(updated_student)
            return students
    return {"message": "Student not found"}
   

@app.delete("/deletestudent")
def deleteStudent(studentid:int):
    global students
    for delete in students:
        if delete["id"] == studentid:
            students.remove(delete)
            return students
    






def start():
    uvicorn.run("class_1.main:app", host="127.0.0.1",port=8080, reload=True)