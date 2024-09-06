
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
    x = s.split()
    if x[0] == "0":
        return n - 0 - int(x[5])
    if x[0] == "1":
        return n - 1 - int(x[5])
    if x[0] == "2":
        return n - 2 - int(x[5])
    if x[0] == "3":
        return n - 3 - int(x[5])
    if x[0] == "4":
        return n - 4 - int(x[5])
    if x[0] == "5":
        return n - 5 - int(x[5])
    if x[0] == "6":
        return n - 6 - int(x[5])
    if x[0] == "7":
        return n - 7 - int(x[5])
    if x[0] == "8":
        return n - 8 - int(x[5])
    if x[0] == "9":
        return n - 9 - int(x[5])
