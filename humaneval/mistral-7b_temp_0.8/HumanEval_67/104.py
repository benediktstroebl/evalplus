
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
    # Use the provided method to complete the exercise
    # You can not change the signature of the method
    # Use the following regex to find the apples and the oranges
    # pattern = r"(\d+)\s+(\w+)s?"
    pattern = r"(\d+)\s+(\w+)"
    # Use the method split to separate the apples and the oranges
    # to the string array
    # and use the method int to convert the string to integer
    # and count the total number of the fruits
    # Then calculate the mango fruits in the basket
    apples, oranges = 0, 0
    fruits = s.split()
    for i in fruits:
        apples += int(i[0])
        oranges += int(i[1][0])
    mangos = n - apples - oranges
    return mangos
