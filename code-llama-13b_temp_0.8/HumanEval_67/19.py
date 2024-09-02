
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
    try:
        if s.find("apples") != -1:
            a = s.find("apples") - 1
            s = s.replace("apples", "")
            s = s.replace(" ", "")
            s = s.replace("and", "")
            if s.find("oranges") != -1:
                o = s.find("oranges") - 1
                s = s.replace("oranges", "")
            else:
                o = 0
            if int(a) + int(o) >= n:
                return n - int(a) - int(o)
            else:
                return "Not enough fruit"
        elif s.find("oranges") != -1:
            a = 0
            s = s.replace("oranges", "")
            s = s.replace(" ", "")
            s = s.replace("and", "")
            if s.find("oranges") != -1:
                o = s.find("oranges") - 1
                s = s.replace("oranges", "")
            else:
                o = 0
            if int(a) + int(o) >= n:
                return n - int(a) - int(o)
            else:
                return "Not enough fruit"
        else:
            return "Not enough fruit"
    except:
        return "Incorrect format"
