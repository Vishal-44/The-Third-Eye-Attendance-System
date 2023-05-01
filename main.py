#import library required.
import tkinter as tk

#-------------------------------------------------------------------------------------------------------------------------------------
def create_main_window():

    # Creating main window(container).
    mainWindow = tk.Tk()
    print('done creating main window')



    # defining main window size.
    #mainWindow.config(width = 1280 , height = 780)


    # defing size to main window.
    mainWindow.title('Attendance Recognition System')

    # adding buttons.
    addStudent = tk.Button(mainWindow , text = 'Add Student', height = 4 , width = 20  , fg = '#000' , borderwidth='4' ,)
    addStudent.pack()


    mainWindow.mainloop() 

#--------------------------------------------------------------------------------------------------------------------------------------

# main function
def main():
    create_main_window()

#-------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

#--------------------------------------------------------------------------------------------------------------------------------------