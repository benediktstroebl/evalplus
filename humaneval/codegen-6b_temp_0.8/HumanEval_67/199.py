
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
    # length of string
    l = len(s)
    # index of "apples"
    p1 = s.find("apples")
    # index of "oranges"
    p2 = s.find("oranges")
    # index of "mangoes"
    p3 = s.find("mangoes")
    # number of "apples"
    n1 = int(s[p1:p1+3])
    # number of "oranges"
    n2 = int(s[p2:p2+3])
    # number of "mangoes"
    n3 = int(s[p3:p3+3])
    # total number of fruits in the basket
    n = int(s[0:l])
    # total number of mango fruits in the basket
    n_mangoes = n - n1 - n2
    return n_mangoes - n3
