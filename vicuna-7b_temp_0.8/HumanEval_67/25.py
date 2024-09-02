
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
    n = int(n)
    if n < 1 or n > 100:
        return -1
    if s == "":
        return -1
    if s[0] == '0' and s[1:] == "0":
        if len(s) < 3:
            return -1
        n1 = int(s[2:])
        n2 = int(s[3:])
        if n1 > 9 or n2 > 9:
            return -1
        if n1 > n2:
            fruit = n1
        else:
            fruit = n2
        return fruit - n1 - n2
    else:
        fruit = int(s[1:])
        return fruit - int(s[2:]) - int(s[3:])
