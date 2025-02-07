# Import modules
from tkinter import *
from tkinter import filedialog
import os
import shutil


# Class for GUI
class GUI(Tk):


    # To set the dimensions of the window
            def _init_(self):
                        super()._init_()
                        self.geometry('400x200')


    # To get the path, Ask for a directory, and return the file name
            def gettingPath(self):
                        self.path = filedialog.askdirectory()
                        return self.path


    # Construction of a button to start the operation
            def startButton(self, path_value):
                        self.button_Frame = Frame(self)
                        self.button_Frame.pack()
                        self.start_Button = Button(self.button_Frame, text='Start', command=lambda: self.startOperation(path_value)).grid(row=0, column=0)


    # To organize files
            def startOperation(self, path_value):
                        count = 0
                        os.chdir(path_value)
                        self.file_list = os.listdir()
                        no_of_files = len(self.file_list)


        # To check if the folder is empty
                        if len(self.file_list) == 0:
                                    self.error_label = Label(text="Error!! Empty folder").pack()
                                    exit()
                        for file in self.file_list:


            # To create a folder for PNG extension images
                                    if file.endswith(".jpg"):
                                                self.dir_name = "JPGFiles"
                                                self.new_path = os.path.join(path_value, self.dir_name)
                                                self.file_list = os.listdir()
                                                if self.dir_name not in self.file_list:
                                                            os.mkdir(self.new_path)
                                                shutil.move(file, self.new_path)


            # To create a folder for txt extension files
                                    elif file.endswith(".txt"):
                                                self.dir_name = "TextFiles"
                                                self.new_path = os.path.join(path_value, self.dir_name)
                                                self.file_list = os.listdir()
                                                if self.dir_name not in self.file_list:
                                                            os.mkdir(self.new_path)
                                                shutil.move(file, self.new_path)
                                                
                                                
                                    elif file.endswith(".pdf"):
                                                self.dir_name = "PDFFiles"
                                                self.new_path = os.path.join(path_value, self.dir_name)
                                                self.file_list = os.listdir()
                                                if self.dir_name not in self.file_list:
                                                            os.mkdir(self.new_path)
                                                shutil.move(file, self.new_path)
                                                
                                                
                                    elif file.endswith(".mp4"):
                                                self.dir_name = "mp4Files"
                                                self.new_path = os.path.join(path_value, self.dir_name)
                                                self.file_list = os.listdir()
                                                if self.dir_name not in self.file_list:
                                                            os.mkdir(self.new_path)
                                                shutil.move(file, self.new_path)
                                                
                                                
                                    count = count+1


                        if(count == no_of_files):
                                    success = Label(text="Files organized Successfuly!").pack()
                        else:
                                    error = Label(text="Failed").pack()


# To run the application
if _name_ == '_main_':
    #allows you to execute code when file is run as script
            object = GUI()
            path = object.gettingPath()
            object.startButton(path)
            object.mainloop()