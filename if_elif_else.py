# demo if...elif...else
def check_num(num):
    if num % 2 == 0:
        print("Number {} is even".format(num))
    elif num % 2 == 1:
        print("Number {} is odd".format(num))
    else:
        print("Number {} is not natural".format(num))

while True:
    while True:
        try:
            num = float(input("Enter a number please: "))
            break
        except ValueError:
            print("Idiot, you shall input an integer or a float, NOT string")
            print()
    check_num(num)

    list = ["Y", "YES"]
    play_again = input("Do you want to check more? (Y/N): ".upper())
    if play_again not in list:
        print("Bye!!!")
        break


