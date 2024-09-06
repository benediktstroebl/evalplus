
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
    #first step is to split the given string
    #then split the splitted string into two strings
    #now we have two string that represents the total number of the apples and oranges
    #now we can get the total number of the fruits in the basket by subtracting the total number of the apples and oranges from the given integer
    #now the total number of the mango fruits is the total number of fruits in the basket minus the total number of the apples and oranges
    #now we have the total number of the mango fruits in the basket
    #now we can return the total number of the mango fruits in the basket
    fruits_basket = str.split(s, "and")
    number_of_apples = str.split(fruits_basket[0], "apples")
    number_of_oranges = str.split(fruits_basket[1], "oranges")
    total_number_of_fruits_in_the_basket = n - int(number_of_apples[1]) - int(number_of_oranges[1])
