def get_text():
    try:
        with open("text.txt", "r") as f:
            a = f.readlines()
            for i1, i in enumerate(a):
                if "\n" in i:
                    a[i1] = i[:-1]
            return a
    except:
        print("Something went wrong!")


while True:
    try:
        a = input("Input number: ")
        if a.isdigit():
            text = get_text()
            for i1, i in enumerate(text):
                text[i1] = i.split(" ")
            for i in text:
                if int(i[1]) > int(a):
                    print(f"time - {i[0]} parametr - {i[1]}")
            break
        else:
            print("Please, input only numbers!\n")
    except:
        print("Something isn`t working!")
