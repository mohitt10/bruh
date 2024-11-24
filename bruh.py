#basically you need to use nested dictionaries here
patients = {}
info = {}
#the function below will store the patient details
def addpatient(patient_id, name, disease, age, gender):
    patient[patient_id] = 
    { 'patient_name' : name ,
      'patient_disease' : disease ,
      'patient_age' : age,
      'patient_gender' : gender,
     }
#the function below will store the patient history and info
def info(patient_id, admission_date, duration, status):
    info[patient_id] = 
    { 'admission_date' : admission_date,
      'treatment_duration' : duration,
      'treatment_status' : status,
     }
#deleting patient info
def del_patientrec(patient_id):
    if patient_id in patients:
        del patients[patient_id]
        del info[patient_if]
        print(f"patient {patient_id} deleted")
    else :
        print("Id not found")

    
