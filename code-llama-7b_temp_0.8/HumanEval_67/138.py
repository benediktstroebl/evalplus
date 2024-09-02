
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
    # take input for the string
    s = s.split()
    #check if the first word in the string is the integer of the total number of the fruits or not
    if s[0].isdigit():
        n = int(s[0])
    else:
        n = n
    # add the number of the apples and oranges in the string with the total number of the fruits
    a = int(s[0]) + int(s[2])
    # return the total number of the mango fruits
    return n - a
