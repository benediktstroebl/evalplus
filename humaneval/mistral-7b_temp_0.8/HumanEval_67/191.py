
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

    # Write your code here
    # convert the string to a list and split it by "and"
    # make a list for each element
    basket_list = s.split("and")
    basket_1 = []
    basket_2 = []
    # check for each element if it has "apples" or "oranges"
    for i in basket_list:
        if "apples" in i:
            basket_1.append(int(i.split(" ")[0]))
        else:
            basket_2.append(int(i.split(" ")[0]))
    # subtract each element in the two list to get the number of mangoes
    mangoes = n - sum(basket_1) - sum(basket_2)
    return mangoes

