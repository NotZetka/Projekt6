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
        print(Fore.LIGHTWHITE_EX+"Żeby wczytać z klawiatury wciśnij 1, żeby wczytać z pliku wciśnij 2")
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

chooseInput()