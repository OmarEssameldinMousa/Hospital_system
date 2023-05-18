import random
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


class Hospital:
    def __init__(self):
        self.ourspecializations = {1: "Cardiology", 2: "Oncology", 3: "Neurology",
                                   4: "Pediatrics", 5: "Orthopedics", 6: "Gynecology",
                                   7: "Endocrinology", 8: "Psychiatry", 9: "Radiology",
                                   10: "Dermatology", 11: "Urology", 12: "Nephrology",
                                   13: "Gastroenterology", 14: "Pulmonology", 15: "Infectious Disease",
                                   16: "Hematology", 17: "Rheumatology", 18: "Allergy and Immunology",
                                   19: "Physical Medicine and Rehabilitation", 20: "Emergency Medicine"
                                   }
        self.specializations_patients = {1: [[], [], []], 2: [[], [], []], 3: [[], [], []], 4: [[], [], []],
                                         5: [[], [], []],
                                         6: [[], [], []], 7: [[], [], []], 8: [[], [], []], 9: [[], [], []],
                                         10: [[], [], []],
                                         11: [[], [], []], 12: [[], [], []], 13: [[], [], []], 14: [[], [], []],
                                         15: [[], [], []],
                                         16: [[], [], []], 17: [[], [], []], 18: [[], [], []], 19: [[], [], []],
                                         20: [[], [], []]
                                         }

    def print_all_specializations(self):
        for i in self.ourspecializations:
            print("(", i, ")", self.ourspecializations[i])

    def add_new_patient(self, specialization, name, status):
        if len(self.specializations_patients[specialization][0]) + len(
                self.specializations_patients[specialization][1]) + len(
            self.specializations_patients[specialization][2]) <= 10:
            if status == 2:
                self.specializations_patients[specialization][0].append(name)
            elif status == 1:
                self.specializations_patients[specialization][1].append(name)
            elif status == 0:
                self.specializations_patients[specialization][2].append(name)
        else:
            print("we are sorry the department is full.")

    def Get_next_patient(self, specialization):
        if self.specializations_patients[specialization] == [[], [], []]:
            print("There are no patients in this specializations left! ")
        elif len(self.specializations_patients[specialization][0]) != 0:
            patient_turn = self.specializations_patients[specialization][0][0]
            self.specializations_patients[specialization][0].pop(0)
            return patient_turn
        elif len(self.specializations_patients[specialization][1]) != 0:
            patient_turn = self.specializations_patients[specialization][1][0]
            self.specializations_patients[specialization][1].pop(0)
            return patient_turn
        elif len(self.specializations_patients[specialization][2]) != 0:
            patient_turn = self.specializations_patients[specialization][2][0]
            self.specializations_patients[specialization][2].pop(0)
            return patient_turn

    def remove_leaving_patient(self, specialization, name):
        if name in self.specializations_patients[specialization][0]:
            self.specializations_patients[specialization][0].remove(name)
        elif name in self.specializations_patients[specialization][1]:
            self.specializations_patients[specialization][1].remove(name)
        elif name in self.specializations_patients[specialization][2]:
            self.specializations_patients[specialization][2].remove(name)
        else:
            print("the name does not exist! there is no one with such a name")

    def dummy_data(self):
        lists_of_dummy_names = [
            ['Hassan', 'Nada', 'Hala', 'Eman', 'Mai'],
            ['Yara', 'Khaled', 'Tarek', 'Nermine', 'Dina', 'Asmaa'],
            ['Nour', 'Mona', 'Sara', 'Ghada', 'Ezzat', 'Hossam', 'Ramy'],
            ['Amira', 'Yasmin', 'Mohamed', 'Hala', 'Ali', 'Ramy', 'Hesham'],
            ['Fatma', 'Salma', 'Nermine', 'Rania', 'Ramy', 'Hend'],
            ['Youssef', 'Shaimaa', 'Ghassan', 'Nada', 'Eman', 'Hoda'],
            ['Hala', 'Naglaa', 'Mahmoud', 'Rasha', 'Yara'],
            ['Ahmed', 'Mai', 'Nada', 'Rania', 'Asmaa'],
            ['Mostafa', 'Yara', 'Khaled', 'Hend', 'Hala'],
            ['Hossam', 'Eman', 'Dina', 'Nada', 'Ramy'],
            ['Sara', 'Yasmin', 'Ali', 'Naglaa', 'Tarek', 'Ghada'],
            ['Hend', 'Amira', 'Youssef', 'Ramy', 'Ezzat', 'Hala', 'Mahmoud'],
            ['Nermine', 'Rania', 'Yara', 'Hoda', 'Hesham', 'Asmaa'],
            ['Hala', 'Yasmin', 'Hassan', 'Mona', 'Naglaa'],
            ['Tarek', 'Sara', 'Ramy', 'Hend', 'Rasha'],
            ['Amira', 'Khaled', 'Mai', 'Nada', 'Ghada', 'Mahmoud'],
            ['Youssef', 'Eman', 'Hala', 'Hossam', 'Nada', 'Ramy'],
            ['Yasmin', 'Hend', 'Nermine', 'Ramy', 'Hala', 'Hossam'],
            ['Mona', 'Naglaa', 'Ali', 'Hesham', 'Asmaa'],
            ['Rania', 'Yara', 'Hala', 'Ezzat', 'Dina']
        ]
        counter = 1
        for i in lists_of_dummy_names:
            for j in i:
                random_status = random.randint(0, 2)
                self.add_new_patient(counter, j, random_status)
            counter += 1


# starting implementing the functions into our tkinter
a = Hospital()
a.dummy_data()
root = Tk()
root.iconbitmap('Images/iconHos.ico')

# Photos we will use in Home screen
img = (Image.open("Images/Hospital_photo.jpg"))
resized_image = img.resize((1210, 650), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)


def new_window():
    for xx in root.winfo_children():
        xx.destroy()


def Addition():
    root.title('Add New Patient')

    def drop_menu_fun(kk):
        global spec_add
        spec_add = kk

    Label(root, image=img_Addition).grid(row=0, column=0)

    Added_name = Entry(root, width=30)
    Added_name.place(x=110, y=223)
    name = Label(root, text="Name", bg="#D6EFEB")
    name.place(x=65, y=223)

    specialization_turn = StringVar()
    drop_menu = OptionMenu(root, specialization_turn, *(a.ourspecializations.items()), command=drop_menu_fun)
    drop_menu.place(x=215, y=180)
    specLabel = Label(root, text="Specialization Number: ", bg="#D6EFEB")
    specLabel.place(x=65, y=180)

    clicked = StringVar()
    clicked.set("Normal")
    status = 0
    drop = OptionMenu(root, clicked, "Super Urgent", "Urgent", "Normal")
    if clicked.get() == "Super Urgent":
        status = 2
    elif clicked.get() == "Urgent":
        status = 1
    else:
        status = 0
    drop.place(x=150, y=370)
    Button(root, text="Add", padx=5, pady=35, font=3, bg="#D6EFEB",
           command=lambda: [a.add_new_patient((spec_add[0]), Added_name.get(), status),

                            messagebox.showinfo("Update!",
                                                "a new patient was added, \nname: " + Added_name.get() + "\nstatus: " + clicked.get()),
                            Added_name.delete(0, END)]).place(x=85, y=370)
    Button(root, text="Back to Dashboard", bg="#EDEDED", font=3,
           command=lambda: [new_window(), Home_Dashboard()]).place(x=0, y=0)


def Next():
    root.title('Get Next Patient')
    global new_resized_image, spec, canvas_next

    def call_button_fn(kk):
        global spec
        Call_btn.place(x=725, y=115)
        spec = kk[0]

    canvas_next = Canvas(root, width=1200, height=444)
    canvas_next.pack()
    canvas_next.create_image(0, 0, anchor="nw", image=img_next)

    specialization_turn = StringVar()

    drop_menu = OptionMenu(root, specialization_turn, *(a.ourspecializations.items()), command=call_button_fn)
    drop_menu.place(x=695, y=80)

    canvas_next.create_window(695, 80, anchor="w", window=drop_menu)

    spec_name = Label(root, text="Specialization Number: ", bg="#D6EFEB", font=3)
    canvas_next.create_window(475, 80, anchor="w", window=spec_name)

    def calling_patient_button(spec_in):
        global new_resized_image, canves_next

        canvas_next.create_image(920, 50, anchor="nw", image=new_resized_image)

        canvas_next.create_window(1040, 100, window=(
            Label(root, text=a.Get_next_patient(spec_in) + ", its your turn hurry up!", bg="white")))

    new_resized_image = ImageTk.PhotoImage((Image.open("Images/pngegg.png")).resize((250, 150), Image.LANCZOS))

    Call_btn = Button(root, text="Call", padx=10, pady=5, font=3, bg="#D6EFEB",
                      command=lambda: [calling_patient_button(spec)])

    canvas_next.create_window(0, 0, anchor="nw", window=(
        Button(root, text="Back to Dashboard", bg="#EDEDED", font=3, command=lambda: [new_window(), Home_Dashboard()])))


def Removal():
    def supmit_button_commnad():
        global specialization_num, submit_remove_button

        a.remove_leaving_patient(specialization_num, ch_remove_name_drop_name_var)
        messagebox.showinfo("Update!", "a patinet was removed  \nspecialization: " + a.ourspecializations[
            specialization_num] + "\nname: " + ch_remove_name_drop_name_var)

    def ch_remove_name_drop_command(kk):

        global canvas_remove, ch_remove_name_drop_name_var
        ch_remove_name_drop_name_var = kk
        submit_remove_button = Button(root, text="submit", command=supmit_button_commnad)
        canvas_remove.create_window(1000, 255, anchor="w", window=submit_remove_button)

    def ch_remove_specilization_drop_command(kk):

        global canvas_remove, ch_remove_specilization_drop_var, specializations_patients, ch_remove_name_drop, ch_remove_name_drop_var, specialization_num
        if ("ch_remove_name_drop" in globals()):
            ch_remove_name_drop.destroy()
        else:
            canvas_remove.create_text(945, 200, anchor="e", text="name", fill="black")
        specialization_num = kk[0]

        lis = a.specializations_patients[specialization_num]
        names = []
        for j in range(len(lis)):
            for k in range(len(lis[j])):
                names.append(lis[j][k])
        ch_remove_name_drop_var = StringVar()
        ch_remove_name_drop = OptionMenu(root, ch_remove_name_drop_var, *(names), command=ch_remove_name_drop_command)
        canvas_remove.create_window(950, 200, anchor="w", window=ch_remove_name_drop)

    global root, canvas_remove, background, img_front, ch_remove_specilization_drop, ch_remove_specilization_drop_var, urspecializations
    root.title('Remove Leaving patient')
    new_window()
    canvas_remove = Canvas(root, width=1500, height=750)
    canvas_remove.pack()
    background = ImageTk.PhotoImage(
        (Image.open("./Images/remove_leaving_patient2.jpg")).resize((1500, 750), Image.LANCZOS))
    canvas_remove.create_image(0, 0, anchor="nw", image=background)
    img_front = ImageTk.PhotoImage(Image.new(mode='RGBA', size=(500, 600), color=(115, 152, 189, 200)))
    canvas_remove.create_image(1050, 350, image=img_front)

    # option meny of choosing specilizasion

    ch_remove_specilization_drop_var = StringVar()
    ch_remove_specilization_drop = OptionMenu(root, ch_remove_specilization_drop_var, *(a.ourspecializations.items()), command=ch_remove_specilization_drop_command)
    canvas_remove.create_window(950, 150, anchor="w", window=ch_remove_specilization_drop)
    canvas_remove.create_text(945, 153, anchor="e", text="specializations", fill="black")
    back = Button(root, text="Back to Dashboard", bg="#EDEDED", font=3,
                  command=lambda: [new_window(), Home_Dashboard()])
    canvas_remove.create_window(0, 0, anchor="nw", window=back)


def Displaying():
    root.title('Display All Patients')
    global canvas_dsiplay, background_display
    new_window()

    canvas_dsiplay = Canvas(root, width=1500, height=900)
    canvas_dsiplay.pack()

    background_display = ImageTk.PhotoImage((Image.open("./Images/Display all patients.jpg")).resize((1500, 900), Image.LANCZOS))
    canvas_dsiplay.create_image(0, 0, anchor="nw", image=background_display)

    # tree

    frame = Frame(root)
    tree_scrol = ttk.Scrollbar(frame)
    tree_scrol.pack(side=RIGHT, fill=Y)
    tree = ttk.Treeview(frame, yscrollcommand=tree_scrol.set)
    tree.pack()

    tree_scrol.config(command=tree.yview)

    tree["columns"] = ("name", "specializations", "status")

    tree.column('#0', stretch=NO, width=0)
    tree.column('name', anchor=CENTER, width=200)
    tree.column('specializations', anchor=CENTER, width=200)
    tree.column('status', anchor=CENTER, width=200)

    tree.heading('#0', text='')
    tree.heading('name', text='name', anchor=CENTER)
    tree.heading('specializations', text='specializations', anchor=CENTER)
    tree.heading('status', text='status', anchor=CENTER)

    for i in a.specializations_patients:

        for j in range(len(a.specializations_patients[i])):
            if j == 0:
                for k in range(len(a.specializations_patients[i][j])):
                    tree.insert(parent='', index="end", text='', values=(
                        a.specializations_patients[i][j][k], a.ourspecializations[i], 'Super urgent'))
            elif j == 1:
                for k in range(len(a.specializations_patients[i][j])):
                    tree.insert(parent='', index="end", text='', values=(
                        a.specializations_patients[i][j][k], a.ourspecializations[i], 'Urgent'))
            elif j == 2:
                for k in range(len(a.specializations_patients[i][j])):
                    tree.insert(parent='', index="end", text='', values=(
                        a.specializations_patients[i][j][k], a.ourspecializations[i], 'Normal'))

    ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    canvas_dsiplay.create_window(750, 400, window=frame, height=220)
    back = Button(root, text="Back to Dashboard", bg="#EDEDED", font=3,
                  command=lambda: [new_window(), Home_Dashboard()])
    canvas_dsiplay.create_window(0, 0, anchor="nw", window=back)

def qu():
    global canvas_quit ,background_quit
    new_window()
    canvas_quit = Canvas(root, width=1170, height=391)
    background_quit = ImageTk.PhotoImage((Image.open("./Images/WhatsApp Image 2022-12-16 at 9.28.03 PM (1).jpeg")).resize((1170, 391), Image.LANCZOS))
    canvas_quit.create_image(0,0, anchor="nw", image =background_quit)
    canvas_quit.create_text(600, 100, anchor="nw", text="copyright omar and magdy\n GOOD BYE" , fill="white" ,font=5)
    canvas_quit.pack()
    root.after(2000, root.destroy)



# Home screen widgets
def Home_Dashboard():
    global img_Addition
    global img_next
    root.title('Hospital Dashboard')
    Add_new_patient_button = Button(root, text="Add new patient", bg="#FFC300", padx=55, pady=10, font=3,
                                    command=lambda: [new_window(), Addition()])
    Add_new_patient_button.grid(row=0, column=3)
    Call_next_patient_button = Button(root, text="Call next patient", bg="#EDEDED", padx=65, pady=10, font=3,
                                      command=lambda: [new_window(), Next()])
    Call_next_patient_button.grid(row=0, column=2)
    Display_all_data = Button(root, text="Display all data", command=Displaying, bg="#EDEDED", padx=65, pady=10, font=3)
    Display_all_data.grid(row=0, column=1)
    Remove_leaving_patient = Button(root, text="Remove leaving patient", command=Removal, bg="#EDEDED", padx=55,
                                    pady=10, font=3)
    Remove_leaving_patient.grid(row=0, column=0)
    Label(image=new_image).grid(row=1, column=0, columnspan=4)
    exit_program_button = Button(root, text="End the Program", bg="#EDEDED", padx=525, pady=10, font=3,
                                 command=qu)
    exit_program_button.grid(row=2, column=0, columnspan=4)
    img_Addition = ImageTk.PhotoImage(Image.open("Images/Add_new_patient_photo.png"))
    img_next = ImageTk.PhotoImage(Image.open("Images/next_patient.jpg"))


Home_Dashboard()
root.mainloop()
