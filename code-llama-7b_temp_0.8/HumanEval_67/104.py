
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    # s = "100 apples and 1 oranges"
    # n = 120
    # s = "2 apples and 3 oranges"
    # n = 100
    # s = "0 apples and 1 oranges"
    # n = 3
    # s = "5 apples and 6 oranges"
    # n = 19

    # s = input("enter a string: ")
    # n = int(input("enter a number: "))
    # print(f"{s} and {n}")

    # s = "5 apples and 6 oranges"
    # n = 19

    # split_fruits = s.split(" ")
    # fruit_numbers = split_fruits[0]
    # fruit_names = split_fruits[2]

    apples_index = s.index("apples")
    apples_number = s[:apples_index]

    oranges_index = s.index("oranges")
    oranges_number = s[apples_index+1:oranges_index]

    fruit_count = n - int(apples_number) - int(oranges_number)

    return fruit_count

