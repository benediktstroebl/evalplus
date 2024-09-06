
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

    fruits_dict = {"apples":0,"oranges":0,"mango":0}
    fruits = s.split(" ")
    if len(fruits) > 2:
        return None
    else:
        if fruits[0] == "0":
            fruits_dict["apples"] = 0
        else:
            fruits_dict["apples"] = int(fruits[0])
        if fruits[1] == "0":
            fruits_dict["oranges"] = 0
        else:
            fruits_dict["oranges"] = int(fruits[1])
        if fruits[2] == "0":
            fruits_dict["mango"] = 0
        else:
            fruits_dict["mango"] = int(fruits[2])
    return fruits_dict["mango"] - fruits_dict["apples"] - fruits_dict["oranges"]

