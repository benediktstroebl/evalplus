
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
    #s = "5 apples and 6 oranges"
    #n = 19
    #n = 3

    #s = "0 apples and 1 oranges"
    #n =3

    #s = "2 apples and 3 oranges"
    #n = 100
    #n = 2

    ##1. all(find position(s.index(f)) >= p - f for f in ("apples", "oranges"))
    ##2. all(find position(s.index(f)) >= p - f for f in ("apples", "oranges"))
    ##3. fruits = "apples", "oranges"
    ##4. fruits = "apples", "oranges"
    ##5. fruits = "oranges", "apples"
    ##6. fruits = "oranges", "apples"
    p = s.find("apples")
    if p == -1:
        return 0

    q = s.find("oranges")
    if q == -1:
        return 0

    if p >= n - s.count("apples") and q >= n - s.count("oranges"):
        return n - s.count("apples") - s.count("oranges")

    return 0
