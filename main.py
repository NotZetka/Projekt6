from colorama import Fore

def Find(string,pattern):
    occurs = []
    liczba=0
    for i in range(0,len(string)-len(pattern)+1):
        if(string[i]==pattern[0]):
            temp = string[i:i+len(pattern)]
            if(temp == pattern):
                occurs.append(i)
                liczba+=1
    yield occurs
    yield liczba

def printResult(string,pattern):
    find = Find(string,pattern)
    occurs = next(find)
    liczba = next(find)
    if(len(occurs)==0):
        print("Nie znaleziono patternu w tekście")
    else:
        print("Pattern " + Fore.RED + pattern + Fore.LIGHTWHITE_EX + " występuje w tekście w miejscach:")
        i = 0
        occur = occurs.pop(0)
        while i<len(string):
            if i>=occur:
                print(Fore.RED + string[i:occur+len(pattern)],end='')
                i+=len(pattern)
                if(len(occurs)>0):
                    occur = occurs.pop(0)
                else:
                    occur = len(string)
            else:
                print(Fore.WHITE + string[i:occur],end='')
                i=occur
        for occur in occurs:
            print(Fore.WHITE + string[0:occur],end='')
            print(Fore.RED + string[occur:occur+len(pattern)],end='')
            print(Fore.WHITE + string[occur+len(pattern):])
        print(Fore.WHITE)
    print(Fore.LIGHTWHITE_EX+"Liczba wystąpień: "+Fore.RED+str(liczba))

def validateInput(string,pattern):
    if(len(string)==0):
        print("Tekst nie może być pusty, spróbuj ponownie")
        chooseInput()
    elif(len(pattern)==0):
        print("Pattern nie może być pusty, spróbuj ponownie")
        chooseInput()
    elif(len(pattern)>len(string)):
        print("Pattern nie może byc dłuższy niż tekst, spróbuj ponownie")
        chooseInput()
    else:
        printResult(string,pattern)

def readFromFile():
    print("Wybrano wczytanie z pliku")
    with open('input.txt') as f:
        line = f.readline()
    line = line.split()
    if(len(line)<2):
        print("Plik jest niepoprawny, spróbuj wczytać z klawiatury")
        readFromKeyboard()
    else:
        string, pattern = line[0],line[1]
        validateInput(string,pattern)

def readFromKeyboard():
    print("Wybrano wczytanie z klawiatury")
    print("Podaj tekst który chcesz przeszukać")
    string = input().strip()
    print("Podaj pattern który chcesz znaleźć")
    pattern = input().strip()
    validateInput(string,pattern)

def chooseInput():
    try:
        print(Fore.LIGHTWHITE_EX+"Żeby wczytać z klawiatury wciśnij 1, żeby wczytać z pliku 'input.txt' wciśnij 2")
        n = int(input())
        if(n==1):
            readFromKeyboard()
        elif(n==2):
            readFromFile()
        else:
            print("Wpisano niepoprawną wartość, spróbuj ponownie")
            chooseInput()
    except:
        print("Błąd, spróbuj ponownie")
        chooseInput()

# używanie konsoli
#chooseInput()




#GUI
def add_GUI():
    import tkinter as tk

    def on_submit():
        try:
            string = text1.get("1.0", "end-1c")
            pattern = text2.get("1.0", "end-1c")
            find = Find(string, pattern)
            occurs = next(find)
            liczba = next(find)
            if (len(occurs) == 0):
                result_label.config(text="Nie znaleziono patternu w tekście")
            else:
                for i in range(0, len(occurs)):
                    text1.tag_add("red", "1." + str(occurs[i]), "1." + str(len(pattern) + occurs[i]))
                text1.tag_config("red", foreground="red")
                result_label.config(
                    text=f"Pattern {pattern} występuje w tekście w miejscach: {occurs}\n Liczba wystąpień: {liczba}")

        except:
            result_label.config(
                text=f"Błąd: wpisz tekst")

    def on_file_select():
        try:
            with open('input.txt') as f:
                line = f.readline()
            line = line.split()
            if (len(line) < 2):
                result_label.config(text="Plik jest niepoprawny, spróbuj wczytać z klawiatury")
            else:
                string, pattern = line[0], line[1]
                text1.delete("1.0", tk.END)
                text1.insert("1.0", string)
                text2.delete("1.0", tk.END)
                text2.insert("1.0", pattern)
                on_submit()

        except:
            result_label.config(text="Błąd, spróbuj ponownie")

    def on_keyboard_select():
        text1.delete("1.0", tk.END)
        text2.delete("1.0", tk.END)
        result_label.config(text="Podaj tekst który chcesz przeszukać")

    root = tk.Tk()
    root.title("Znajdź pattern w tekście")

    label1 = tk.Label(root, text="Tekst:")
    label1.grid(row=0, column=0)

    text1 = tk.Text(root, height=5, width=30)
    text1.grid(row=1, column=0)

    label2 = tk.Label(root, text="Pattern:")
    label2.grid(row=2, column=0)

    text2 = tk.Text(root, height=2, width=30)
    text2.grid(row=3, column=0)

    submit_button = tk.Button(root, text="Znajdź", width=16,command=on_submit)
    submit_button.grid(row=4, column=0)

    file_button = tk.Button(root, text="Wczytaj z pliku" ,width=16, command=on_file_select)
    file_button.grid(row=5, column=0)

    keyboard_button = tk.Button(root, text="Wczytaj z klawiatury", width=16, command=on_keyboard_select)
    keyboard_button.grid(row=6, column=0)

    result_label = tk.Label(root)
    result_label.grid(row=7, column=0)

    root.mainloop()


#start program
add_GUI()