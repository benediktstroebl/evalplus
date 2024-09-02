
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

    count_fruits = s.split(" ")
    count_oranges = int(count_fruits[0])
    count_apples = int(count_fruits[1])
    
    if n >= count_oranges and n >= count_apples:
        return int(n - count_oranges - count_apples)
    elif n >= count_oranges and n < count_apples:
        return int(n - count_oranges)
    elif n < count_oranges and n >= count_apples:
        return int(n - count_apples)
    elif n < count_oranges and n < count_apples:
        return int(n)


