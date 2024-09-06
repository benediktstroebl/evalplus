
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
    if not isinstance(s,str):
        return "s isn't a string"
    try:
        n=int(n)
    except:
        return "n isn't a number"
    if n<0:
        return "n is negative"
    s=s.lower()
    splited=s.split()
    if "orange" not in splited and "apple" not in splited:
        return "no oranges or apples"
    if splited.count("orange")>1 or splited.count("apple")>1:
        return "too many oranges or apples"
    if "orange" in splited:
        oranges=int(splited[splited.index("orange")-1])
    else:
        oranges=0
    if "apple" in splited:
        apples=int(splited[splited.index("apple")-1])
    else:
        apples=0
    if apples+oranges>n:
        return "too many fruit"
    return n-apples-oranges
