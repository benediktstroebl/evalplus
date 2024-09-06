
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
    if int(n) < 0:
        return 0
    elif int(n) == 0:
        return 0
    else:
        n_fruit = int(n)
        for i in range(int(s[:s.find(' and ')]),n_fruit):
            n_fruit = n_fruit - i
        if n_fruit == 0:
            return 0
        else:
            return int(n_fruit - (n_fruit*0.25))






