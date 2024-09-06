
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
    if not isinstance(s,str) or not isinstance(n,int):
        return 'Invalid Inputs'
    arr = s.split()
    if len(arr) != 5:
        return 'Invalid Inputs'
    if arr[0] != "0" and arr[0] != "1" and arr[0] != "2" and arr[0] != "3":
        return 'Invalid Inputs'
    if arr[2] != "apples" or arr[4] != "oranges":
        return 'Invalid Inputs'
    if not arr[1].isdigit() or not arr[3].isdigit():
        return 'Invalid Inputs'
    return n - int(arr[1]) - int(arr[3])

