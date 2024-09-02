
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
    apples_and_oranges = s.split()
    if len(apples_and_oranges) < 1 or len(apples_and_oranges) > 100:
        return -1
    oranges_and_apples = []
    for fruit in apples_and_oranges:
        if fruit == "a":
            oranges_and_apples.append(1)
        elif fruit == "o":
            oranges_and_apples.append(2)
        elif fruit == "m":
            oranges_and_apples.append(3)
        else:
            print("Invalid fruit")
    for i in range(len(oranges_and_apples)):
        oranges_and_apples[i] = oranges_and_apples[i] * (i+1)
    total_oranges = sum(oranges_and_apples)
    total_apples = sum(oranges_and_apples) - sum(oranges_and_apples[:-1])
    total_fruits = sum(oranges_and_apples)
    mango_fruits = total_fruits - total_oranges
    return mango_fruits