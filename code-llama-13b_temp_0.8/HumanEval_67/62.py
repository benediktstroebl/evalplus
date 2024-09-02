
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
    # your code here
    # use the replace function to replace the space in the string with nothing so it will be easy to get the numbers
    s = s.replace(' ','')
    # split the string to get the numbers of the apples and oranges in the basket
    bask = s.split('and')
    # get the numbers of the apples and oranges
    apples = int(bask[0])
    oranges = int(bask[1])
    # calculate the number of the mango fruits
    mangos = n - apples - oranges
    # return the number of the mango fruits
    return mangos
