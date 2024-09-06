
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

    
    if s.find('apples') == -1:
        s +='apples'
    if s.find('oranges') == -1:
        s +='oranges'
    total = 0
    total_fruits = 0
    total_fruits += int(s[s.index('apples')+7:s.index('apples')+8])
    total_fruits += int(s[s.index('oranges')+8:s.index('oranges')+9])
    total += total_fruits
    total += int(s[s.index('mango')+7:s.index('mango')+8])
    if total!= n:
        return total - n
    return total - n + int(s[s.index('mango')+7:s.index('mango')+8])

