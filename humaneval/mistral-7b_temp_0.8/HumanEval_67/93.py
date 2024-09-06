
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
    s = s.split()
    sum_apple = 0
    sum_orange = 0
    sum_mango = 0
    for i in s:
        if "apples" in i:
            sum_apple += int(i.split(" ")[0])
        elif "orange" in i:
            sum_orange += int(i.split(" ")[0])
        elif "mango" in i:
            sum_mango += int(i.split(" ")[0])
    sum_mango += n - sum_apple - sum_orange
    return sum_mango
