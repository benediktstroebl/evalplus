
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
    def is_mango(c):
        a="apples"
        o="oranges"
        m="mango"
        return (c.lower() == m)
    def is_apples(c):
        a="apples"
        o="oranges"
        m="mango"
        return (c.lower() == a)
    def is_oranges(c):
        a="apples"
        o="oranges"
        m="mango"
        return (c.lower() == o)
    basket = s.split()
    for i in range(len(basket)):
        if is_mango(basket[i]):
            n=n-1
        elif is_apples(basket[i]):
            n=n-2
        elif is_oranges(basket[i]):
            n=n-3
    return n
