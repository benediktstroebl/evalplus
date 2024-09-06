
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
    fruits_list = s.split()
    basket_apples, basket_oranges = fruits_list[0].split(' and ')
    basket_apples, basket_oranges, basket_mango = list(map(int, (basket_apples.split(' '), basket_oranges.split(' '), basket_mango.split(' '))))

    if basket_apples + basket_oranges < n:
        return basket_mango
    else:
        return n - (basket_apples + basket_oranges)
