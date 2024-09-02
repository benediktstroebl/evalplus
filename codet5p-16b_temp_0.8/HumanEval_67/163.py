
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

    
    fruit_list = s.split(' ')
    orange_numbers = int(fruit_list[0])
    apple_numbers = int(fruit_list[2])
    orange_apples = 0
    apple_oranges = 0
    for i in fruit_list:
        if i.startswith("o"):
            orange_apples += int(i[1:])
        elif i.startswith("a"):
            apple_oranges += int(i[1:])
    print(orange_apples, apple_oranges)

    return (orange_numbers - apple_numbers - orange_apples) - (orange_apples - apple_oranges)
