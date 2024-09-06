
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
    fruit_type_list = s.split()
    number_of_apples = 0
    number_of_oranges = 0
    number_of_mangos = 0
    number_of_fruits = 0
    if "apples" in fruit_type_list[0]:
        number_of_apples = int(fruit_type_list[0].split(" ")[1])
    if "oranges" in fruit_type_list[1]:
        number_of_oranges = int(fruit_type_list[1].split(" ")[1])
    if "mangos" in fruit_type_list[2]:
        number_of_mangos = int(fruit_type_list[2].split(" ")[1])
    number_of_fruits = number_of_apples + number_of_oranges + number_of_mangos
    return n - number_of_fruits
