import os
class Folder:
    def __init__(self):
        self.path_history = []

    def read_folder(self,input1):
        l=f"{input1}:/"
        path = os.path.normpath(l)
        self.path = path

        if not os.path.exists(path):
            print("folder not found")
            return

        p = os.listdir(path)
        self.p = p
        for index,v in enumerate(p,start=1):
            print(f"{index}---->{v}")
            
    def enter_folder(self):
        enter_folder_input=int(input("enter your choise: "))
        e=self.p[enter_folder_input-1]
        path_enter = os.path.join(self.path, e)
        self.path_history.append(self.path)
        a = os.listdir(path_enter)
        for index, item in enumerate(a, start=1):
            print(f"{index}---->{item}")
        self.path = path_enter
        
    def make_folder(self):
        make_folder_input=str(input("enter your folder name: "))
        path = os.path.join(self.path, make_folder_input)
        os.mkdir(path)
        print("Folder creat")
    def remove_folder(self):
        remove_folder_input=str(input("enter your folder name: "))
        path1= os.path.join(self.path,remove_folder_input) 
        os.rmdir(path1)
    def make_text(self):
        make_text_input=str(input("enter your text name: "))
        text_in_input=str(input("enter your text in file: "))
        file_path = os.path.join(self.path, f"{make_text_input}.txt")
        with open(file_path,"w", encoding="utf-8") as f:
            f.write(f"{text_in_input}")
    def update_text(self):
        update_text_input1=str(input("enter your text name: "))
        file_path1 = os.path.join(self.path, f"{update_text_input1}.txt")
        if os.path.exists(file_path1):
            with open(file_path1,"r") as f:
                old_text=f.read()
                print("-----File Content-----")
                print(old_text)
                print("----------------------")
        else:
            print("File not found.")
            return
        new_text = str(input("enter your new text: "))
        with open(file_path1,"a") as f:
            f.write("\n" + new_text)
    def reader_text(self):
        reader_folder_input = str(input("enter your file name: "))
        path2 = os.path.join(self.path, f"{reader_folder_input}.txt")

        if os.path.exists(path2):
            with open(path2, "r", encoding="utf-8") as f:
                file = f.read()
                print("----File Content---")
                print(file)
                print("-------------------")

        else:
            print("file not found")
    def remove_text(self):
        remove_text_input = str(input("enter your file name: "))
        path2 = os.path.join(self.path, f"{remove_text_input}.txt")
        os.remove(path2)
    def back(self):
        path3 = list[path4]
        path3 = path3.pop()
        self.path = path3
        a = os.listdir(self.path)
        for index, item in enumerate(a, start=1):
            print(f"{index}---->{item}")

    def back(self):
        last_path = self.path_history.pop()
        self.path = last_path
        a = os.listdir(self.path)
        self.p = a
        print("\n--- Back to Previous Folder ---")
        for index, item in enumerate(a, start=1):
            print(f"{index}---->{item}")


def main():
    folder=Folder()
    input1=str(input("enetr your folder(f.e. c or d): "))
    folder.read_folder(input1)
    while True:
        print(f"........\n1.Make folder \n2.Remove folder \n3.Make text \n4.Update text \n5.Reader text \n6.Remove text \n7.Enter Folder \n8.Back")
        input2=int(input("enter your chiose: "))
        if input2 == 1:
            folder.make_folder()
        elif input2 == 2:
            folder.remove_folder()
        elif input2 == 3:
            folder.make_text()
        elif input2 == 4:
            folder.update_text()
        elif input2 == 5:
            folder.reader_text()
        elif input2 == 6:
            folder.remove_text()
        elif input2 == 7:
            folder.enter_folder()
        elif input2 == 8:
            folder.back()

    
if __name__=="__main__":
    main()

