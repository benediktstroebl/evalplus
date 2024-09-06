
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
    # this solution will be a little bit lengthy but it will work.
    # first I will split the string to make it easier to work with.
    # then I will iterate on each element of the list and I will check if the element contains 
    # the string "apples" or "oranges" if it contains that element I will subtract the number 
    # in the string from the total.
    # then I will return the rest of the fruits in the basket
    result = n
    lst = s.split()
    for i in lst:
        if "apples" in i:
            result -= int(i.split("apples")[0])
        elif "oranges" in i:
            result -= int(i.split("oranges")[0])
    return result
