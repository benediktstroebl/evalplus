
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

    if not isinstance(n,int):
        raise TypeError("The number should be an integer")
    if not isinstance(s,str):
        raise TypeError("The string should be a string")
    if n < 0:
        raise ValueError("The number should be positive")
    if s.find('and')==-1:
        raise ValueError("The string should contain two number and")
    if s.find('apples') == -1 or s.find('oranges') == -1:
        raise ValueError("The string should contain two numbers")
    if s.find('apples') > s.find('oranges'):
        raise ValueError("The string should contain two numbers")
    if n < s.find('apples') + s.count('apples') + s.find('oranges') + s.count('oranges'):
        raise ValueError("The number of the fruits is more than the basket")

    return s.count('mango')
