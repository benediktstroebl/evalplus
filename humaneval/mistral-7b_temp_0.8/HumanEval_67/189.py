
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
    fruit_num = 0
    fruit_list = []
    fruit_list_in = s.split(" and ")
    fruit_list_in_1 = fruit_list_in[0].split(" ")
    for num in fruit_list_in_1:
        if num == "apples":
            fruit_num = fruit_num + int(num.split(" ")[0])
        if num == "oranges":
            fruit_num = fruit_num + int(num.split(" ")[0])
        if num == "mango":
            fruit_num = fruit_num + int(num.split(" ")[0])
    fruit_list_in_2 = fruit_list_in[1].split(" ")
    for num in fruit_list_in_2:
        if num == "apples":
            fruit_num = fruit_num + int(num.split(" ")[0])
        if num == "oranges":
            fruit_num = fruit_num + int(num.split(" ")[0])
        if num == "mango":
            fruit_num =
