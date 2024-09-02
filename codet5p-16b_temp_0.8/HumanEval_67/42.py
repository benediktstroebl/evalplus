
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

    fruit = { "apple" : "apples", "orange" : "oranges", "mango" : "mangoes"}
    result = s.split(" ")
    result = [int(x) for x in result]
    print(result)
    sum_of_fruits = sum(result)
    print(sum_of_fruits)
    sum_of_fruits -= (result[1]*2) + (result[2]*3) + (result[0]*4)
    print(sum_of_fruits)
    for key,value in fruit.items():
        if key in s:
            sum_of_fruits -= result[fruit[key]]
    print(sum_of_fruits)
    return sum_of_fruits
