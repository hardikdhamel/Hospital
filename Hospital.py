class Hospital:
    def __init__(self):
        self.choice = 0
        self.id = 1234
        self.user_type = 0
        self.name = []
        self.disease = []
        self.mono = []
        self.statusofpatient = []
        self.dob = []
        self.date = []
        self.allotedroom = []
        self.admit = 0
        self.name1 = []
        self.mono1 = []
        self.dob1 = []
        self.doctor = []
        self.timings = []
        self.appointment = 0
        self.listofdoctors = ['DR.PRATIK SHARMA', 'DR.JOHM SMITH', 'DR.KALPESH TRIVEDI', 'DR.NEHA YADAV', 'DR.HARDIK PANDYA']
        self.listoftimings = [9.00, 11.00, 1.00, 3.00, 5.00]
        self.leavestatus = [0, 0, 0, 0, 0]
        self.room = ['1-a', '1-b', '1-c', '2-a', '2-b', '2-c']
        self.roomstatus = [0, 0, 0, 0, 0, 0]
        self.userdoctor = ''
        self.dischargingTime = []
        self.TotalExpance = []

    def admitdetailsofpatient(self):
        print("--------------------------------------------------------------")
        print("| Sr No | Name            | Room No | Status    | Disease     |")
        print("--------------------------------------------------------------")
        for i in range(len(self.name)):
            print(f"| {i+1:<6} | {self.name[i]:<15} | {self.allotedroom[i]:<8} | {self.statusofpatient[i]:<9} | {self.disease[i]:<11} |")
        print("--------------------------------------------------------------")

    def checkappointments(self):
        find_name = input('Enter the name of the patient: ')
        flag = 0
        for i in range(self.appointment):
            if find_name == self.name1[i]:
                flag += 1
                doctor_index = self.doctor[i]  
                print("--------------------------------------------------------------")
                print(f"Patient Name: {self.name1[i]}")
                print(f"Doctor Name: {self.listofdoctors[doctor_index]}")
                print(f"Timings: {self.timings[i]}")
                print("--------------------------------------------------------------")
        if flag == 0:
            print('Patient not found')

    def checkrooms(self):
        count = 0
        temp = 0
        flag = 0
        roomchoice = int(input('Enter 1 to allot a room, or 2 to cancel:'))
        name = input('Enter the name of the patient:')
        for i in range(len(self.name)):
            if self.name[i] == name:
                count += 1
                temp = i
                flag += 1
        if flag == 0:
            print('No patient found')
            return 0
        if roomchoice == 1:
            for i in range(len(self.roomstatus)):
                if self.roomstatus[i] == 0:                  
                    print('Alloted room is ', self.room[i])
                    self.allotedroom[temp] = self.room[i]
                    self.roomstatus[i] = 1
                    count += 1
                    print(self.allotedroom[temp])
                    break
            else:
                print('Sorry, no rooms are available')
                return 0   
        elif roomchoice == 2:
            if self.allotedroom[temp]:  
                for i in range(len(self.room)):
                    if self.allotedroom[temp] == self.room[i]: 
                        self.roomstatus[i] = 0  
                        self.allotedroom[temp] = 'null'
                        print("Room assignment canceled successfully.")
                        break
            else:
                print("No room assigned to cancel.")
        else:
            print("Invalid choice")


    def usertype(self):
        self.user_type = int(input('PRESS 1 IF YOU ARE STAFF OR PRESS 2 IF YOU ARE DOCTOR'))
        if self.user_type == 2:
            return True 
        elif self.user_type == 1:
            return False
        else:
            raise Exception('Invalid choice')
    def staff_functions(self):
            print("--------------------------------------------------------------")
            print("|                     User Functions Menu                    |")
            print("--------------------------------------------------------------")
            print("| 1. Admit Patient                                           |")
            print("| 2. Take Appointments                                       |")
            print("| 3. Check Rooms                                             |")
            print("| 4. Update Patients                                         |")
            print("| 5. Discharge Patient                                       |")
            print("| 6. Admitted Details of Patient                             |")
            print("| 7. View Record                                             |")
            print("| 8. Make Final Bill                                         |")
            print("| 9. Check Appointments                                      |")
            print("| 10. Exit                                                   |")
            print("| 11. Back to User Type Selection                            |")
            print("--------------------------------------------------------------")
            self.choice = int(input('Enter your choice: '))


    def doctor_functions(self):
            print("--------------------------------------------------------------")
            print("|                   Doctor Functions Menu                    |")
            print("--------------------------------------------------------------")
            print("| 1. Take Leave                                              |")
            print("| 2. Come Back to Work                                       |")
            print("| 3. Check Your Appointments                                 |")
            print("| 10. Exit                                                   |")
            print("| 4. Back                                                    |")
            print("--------------------------------------------------------------")
            self.choice = int(input('Enter your choice: '))

    def check_id(self):
        id_input = int(input('Enter your staff ID: '))
        if id_input == self.id:
            return True
        else:
            return False

    def take_appointments(self):
        print("List of Doctors:")
        for i, doctor in enumerate(self.listofdoctors):
            print(f"{i + 1}: {doctor}")
        doctor_choice = int(input("Enter the number corresponding to the doctor you want to book an appointment with:"))

        if doctor_choice < 1 or doctor_choice > len(self.listofdoctors):
            print("Invalid doctor choice")
            return

        doctor_index = doctor_choice - 1

        if self.leavestatus[doctor_index] == 1:
            print(f"{self.listofdoctors[doctor_index]} IS NOT AVAILABLE FOR NOW")
            return

        name = input("Enter the name of the patient:")
        dob = input("Enter the date of birth of the patient in dd/mm/yyyy format:")
        mobile_number = input("Enter the mobile number of the patient:")
        self.name1.append(name)
        self.dob1.append(dob)
        self.mono1.append(mobile_number)
        self.doctor.append(doctor_index)
        self.appointment+=1
        next_timing = None
        for i, timing in enumerate(self.listoftimings):
            if self.leavestatus[i] == 0 and timing not in self.timings:
                next_timing = timing
                self.timings.append(next_timing)
                break

        if next_timing is None:
            print("Sorry, no available timing slot for this doctor")
            return

        print("Appointment booked successfully:")
        print(f"Doctor: {self.listofdoctors[doctor_index]}")
        print(f"Timing: {next_timing}")


    def admit_patient(self):
        self.name.append(input('Enter the name of the patient: '))
        self.disease.append(input('Enter the name of the disease: '))
        self.mono.append(input('Enter the mobile number of the patient: '))
        self.dob.append(input('Enter the birth-date of the patient in dd/mm/yy format: '))
        self.statusofpatient.append('ADMITTED')
        self.allotedroom.append('null')
        self.admit += 1
        self.TotalExpance.append(0)
        self.date.append(0)

    def update_patients(self):
        choice_update = int(input('If you want to update the detail of the appointment then press 1 else press 2: '))
        count = 0
        if choice_update == 1:
            findname = input('Enter the name of the patient: ')
            for i in range(len(self.name1)):
                if findname.lower() == self.name1[i].lower():
                    count += 1
                    print('For change in name enter 1.')
                    print('For change in dob enter 2.')
                    print('For change in mobile no. enter 3')
                    choice = int(input('Enter the choice: '))
                    if choice == 1:
                        self.name1[i] = input('Enter the name of the patient: ')
                        break
                    elif choice == 2:
                        self.dob1[i] = input('Enter the date: ')
                        break
                    elif choice == 3:
                        self.mono1[i] = input('Enter the mobile number of the patient: ')
                        break
                    else:
                        print('Enter valid choice')
                        break
            else:
                print('Patient not found')
        else:
            findname = input('Enter the name of the patient: ')
            for i in range(len(self.name)):
                if findname.lower() == self.name[i].lower():
                    count += 1
                    print('For change in name enter 1.')
                    print('For change in D.O.B enter 2.')
                    print('For change in mobile no. enter 3')
                    print('For change in disease enter 4')
                    choice = int(input('Enter the choice: '))
                    if choice == 1:
                        self.name[i] = input('Enter the new name of the patient: ')
                        break
                    elif choice == 2:
                        self.dob[i] = input('Enter the new DOB of the patient in dd/mm/yy format: ')
                        break
                    elif choice == 3:
                        self.mono[i] = input('Enter the new mobile number of the patient: ')
                        break
                    elif choice == 4:
                        self.disease[i] = input('Enter the new name of the disease: ')
                        break
                    else:
                        print('Enter valid choice')
                        break
            else:
                print('Patient not found')

    def view_record(self):
        print("Admitted Patients:")
        self.admitdetailsofpatient()
        print("\nAppointments:")
        print("--------------------------------------------------------------")
        print("| Sr No | Doctor           | Date       | Name       | Mobile No  |")
        print("--------------------------------------------------------------")
        for i in range(len(self.name1)):
            self.doctor_index = self.doctor[i]  
            self.doctor_name = self.listofdoctors[self.doctor_index]  
            print(f"| {i+1:<6} | {self.doctor_name:<15} | {self.dob1[i]:<10} | {self.name1[i]:<10} | {self.mono1[i]:<10} |")
        print("--------------------------------------------------------------")

    def discharge_patient(self):
        findname = input('Enter the name of the patient who wants to discharge: ')
        count = 0
        for i in range(self.admit):
            if findname == self.name[i]:
                print('Enter the time of discharging')
                self.dischargingTime.append(input())
                count += 1
                self.date[i] = input('Enter the date: ')
                self.statusofpatient[i] = 'discharged'
                self.roomstatus[i] = 0
        if count == 0:
            print('Name not found')

    def makefinalbill(self):
        find_name = input('Enter the name: ')
        count = 0
        for i in range(self.admit):
            if find_name == self.name[i]:
                self.TotalExpance[i] = int(input('Enter the total expense of the patient: '))
                print("\n====================== BILL ======================")
                print(f"Patient Name: {self.name[i]}")
                print(f"Date of Birth (DOB): {self.dob[i]}")
                print(f"Mobile Number: {self.mono[i]}")
                print(f"Disease: {self.disease[i]}")
                print(f"Total Expense: ${self.TotalExpance[i]}")
                print("===================================================")
                count += 1
        if count == 0:
            print('Patient not found')

    def checkidofdoctor(self):
        id = int(input('Enter your doctor id: '))
        password = [1234, 5678, 7890, 9012, 0000]
        for i in range(len(password)):
            if id == password[i]:
                print('Welcome MR ' + self.listofdoctors[i])
                self.userdoctor = self.listofdoctors[i]
                return True
        else:
            return False

    def takeleave(self):
        print(self.userdoctor + " IS ON LEAVE")
        parameter_of_leave = None
        for i in range(len(self.listofdoctors)):
            if self.userdoctor == self.listofdoctors[i]:
                parameter_of_leave = i
                break
        else:
            print("Doctor not found")
            return

        self.leavestatus[parameter_of_leave] = 1

    def comeback(self):
        print(self.userdoctor + " IS AVAILABLE NOW.")
        parameter_of_leave = None
        for i in range(len(self.listofdoctors)):
            if self.userdoctor == self.listofdoctors[i]:
                parameter_of_leave = i
                break
        else:
            print("Doctor not found")
            return

        self.leavestatus[parameter_of_leave] = 0
    def checkappointmentdoctor(self):
        appointments_exist = False
        print("Your Appointments:")
        print("--------------------------------------------------------------")
        print("| Sr No | Patient Name    | DOB       | Time    |")
        print("--------------------------------------------------------------")
        for i in range(len(self.name1)):
            if self.userdoctor == self.listofdoctors[self.doctor[i]]:
                appointments_exist = True
                print(f"| {i+1:<6} | {self.name1[i]:<15} | {self.dob1[i]:<10} | {self.timings[i]:<8} |")
        if not appointments_exist:
            print("No appointments found")
        print("--------------------------------------------------------------")

class Main:
    h = Hospital()
    h.usertype()
    while True:
        if h.choice == 10:
            break
        if h.user_type == 1:
            b = False
            while True:
                b = h.check_id()
                if b==False:
                    print('Enter valid Id')
                    continue
                else:
                    break
            while True:
                h.staff_functions()
                if h.choice == 1:
                    h.admit_patient()
                elif h.choice == 2:
                    h.take_appointments()
                elif h.choice == 3:
                    h.checkrooms()
                elif h.choice == 4:
                    h.update_patients()
                elif h.choice == 5:
                    h.discharge_patient()
                elif h.choice == 6:
                    h.admitdetailsofpatient()
                elif h.choice == 7:
                    h.view_record()
                elif h.choice == 8:
                    h.makefinalbill()
                elif h.choice == 9:
                    h.checkappointments()
                elif h.choice == 10:
                    break
                elif h.choice == 11:
                    h.usertype()
                    break
                else:
                    pass
        elif h.user_type == 2:
            b = False
            b = h.checkidofdoctor()
            if b:
                while True:
                    h.doctor_functions()
                    if h.choice == 1:
                        h.takeleave()
                    elif h.choice == 2:
                        h.comeback()
                    elif h.choice == 3:
                        h.checkappointmentdoctor()
                    elif h.choice == 4:
                        h.usertype()
                        break
                    elif h.choice == 10:
                        break
                    else:
                        print('Enter valid choice')
            else:
                print('Id does not match')
        else:
            print('Sorry no match for input')