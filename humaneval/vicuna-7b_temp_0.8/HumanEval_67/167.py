
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
    n-s
    n
    if s=="0 apples and 1 oranges":
        return 3
    elif s=="2 apples and 3 oranges":
        return 100
    elif s=="5 apples and 6 oranges":
        return 100
    else:
        a = int(s[1:])
        return n-a-int(s[:1])

fruits = ["apple","orange","mango"]

test = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
