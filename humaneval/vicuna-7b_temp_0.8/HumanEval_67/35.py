
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
    n-s
    s=0
    count_of_fruits=0
    for fruit in fruits:
        if fruit in s:
            count_of_fruits+=1
    
    total_fruits=n
    if fruits.count("oranges")==total_fruits and fruits.count("apples")==0:
        return total_fruits-count_of_fruits
    elif fruits.count("apples")==total_fruits and fruits.count("oranges")==0:
        return count_of_fruits-total_fruits
    elif fruits.count("apples")>fruits.count("oranges"):
        if total_fruits-count_of_fruits>0:
            return count_of_fruits-total_fruits
        else:
            return 0
    elif fruits.count("oranges")>fruits.count("apples"):
        if total_fruits-count_of_fruits<0:
            return total_fruits-count_of_fruits
        else:
            return 0
    else:
        return count_of_fruits
