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
# assigning doctors: 
# the patient id of the patients they are assigned to
# also we need to check that one doctor is assigned only 2 patients at a time
# create a dictonary of doctor names which keeps the track of number of patients assigned
doctor_assigned = {}
def assign_doctor(patient_id,doctor):
    if doctor not in doctor_assigned:
        doctor_assigned[doctor] =[] 
    if len(doctor_assigned[doctor]) < 2:
        doctor_assigned[doctor].append[patient_id]
        print(f'doctor assigned to {patient_id}')
    else:
        print('doctor is already assigned two patients')
# now comes the printing part,whatever the cost is, just multiply it by the duration
# 'bill' is the ammount.also dont forget change the date type of duration before multiplying
def print_bill(patient_id):
    #write the function here
    print(f'The bill for the patient {patient_id} is {bill}')
#status updater:
def set_treatment_status(patient_id,status):
    if patient_id in info:
        info[patient_id][treatment_status] = status
        print("status successfully updated")
    else
        print("no ID found")


