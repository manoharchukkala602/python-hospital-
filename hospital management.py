from datetime import datetime
import json
FILE_NAME = "hospital.json"
def load_data():
    try:
        with open(FILE_NAME,"r") as f:
           return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
            return {
                "patients":[],
                "doctors":[],
                "appointments":[],
                
                }
                     
def save_data(data):
    with open(FILE_NAME,"w") as f:
        json.dump(data,f,indent =4)
data =load_data()

def add_patient():
    data =load_data()
    pid =len(data["patients"])+1
    name =input("Enter patient name:")
    age =int(input("Enter patient age:"))
    disease =input("Enter the disease:")
    doctor =input("Enter doctor name:")

    patient ={
        "id":pid,
        "name":name,
        "age":age,
        "disease":disease,
        "doctor":doctor,
        }
    data["patients"].append(patient)
    save_data(data)
    print("patient is add to cart to check up__")
def view_patient():
    data =load_data()
    if not data["patients"]:
        print("no patients are found in the list")
        return
    for c in data["patients"]:
        print("patient id",c["id"],":","patient name", ":",c["name"],"disease",":",c["disease"],":","doctor",":",c["doctor"])

def add_doctor():
    data =load_data()
    did =len(data["doctors"])+1
    name =input("Enter doctor name:")
    specialization =input("Enter doctor speciliazation:")
    doctor ={
        "id":did,
        "name":name,
        "specialization":specialization,
        }
    data["doctors"].append(doctor)
    save_data(data)
    print("doctors ready for check up")
def view_doctors():
    data=load_data()
    if not data["doctors"]:
        print("no doctors are found")
        return
    for d in data["doctors"]:
        print("doctor name",":",d["name"],":","id",":",d["id"],":","specialization of doctor",":",d["specialization"])

def book_appointment():
    data =load_data()
    if not data["patients"] or  not data["doctors"]:
        print("not found both doctor and patient")
        return
    pid =int(input("Enter patient id:"))
    did =int(input("Enter doctor id:"))
    patient =next((p for p in data["patients"] if p["id"] ==pid),None)
    doctor =next((d for d in data["doctors"] if d["id"]==did),None)
    if not patient or not doctor:
        print("invalid id")
        return
    appointment={
        "patient":patient["name"],
        "doctor":doctor["name"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    data["appointments"].append(appointment)
    save_data(data)
    print("your appointment added successfully")
def view_appoints():
    data=load_data()
    if not data["appointments"]:
        print("no appointments")
        return
    for app in data["appointments"]:
        print("name of patient",":",app["patient"],"name of doctor",":",app["doctor"],"data",":",app["date"])
        print("calling the patient")
while True:
    print("______enter python hospital_______")
    print("1.add patient")
    print("2.view patient")
    print("3.add doctor")
    print("4.view doctor")
    print("5.book appointment")
    print("6.view appointment")
    choice =input("Enter your choice:")
    if choice =="1":
        add_patient()
    elif choice =="2":
        view_patient()
    elif choice =="3":
        add_doctor()
    elif choice =="4":
        view_doctors()
    elif choice =="5":
        book_appointment()
    elif choice == "6":
        view_appoints()
        break
    else:
        print("thank you for visit my python hospital")
    
    
        

        


        
    
             
     
