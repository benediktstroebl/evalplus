
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

    oranges = s.split(" ")[0]
    apples = s.split(" ")[1]
    mangoes = 0
    while int(oranges) > 0:
        if int(oranges) >= 3:
            mangoes += 3
            oranges = oranges - 3
        elif int(oranges) < 3 and int(oranges) >= 1:
            mangoes += int(oranges)
            oranges = 0
        elif int(oranges) == 0:
            mangoes += int(oranges)
            oranges = 0
    
    while int(apples) > 0:
        if int(apples) >= 3:
            mangoes += 3
            apples = apples - 3
        elif int(apples) < 3 and int(apples) >= 1:
            mangoes += int(apples)
            apples = 0
        elif int(apples) == 0:
            mangoes += int(apples)
            apples = 0
    return mangoes
    
