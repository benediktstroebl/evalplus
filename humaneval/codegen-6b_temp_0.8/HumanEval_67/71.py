
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
    assert type(s)==str,"Fruit distribution must be given a string. Given string: {}".format(s)
    assert type(n)==int,"Fruit distribution must be given an integer. Given: {}".format(n)
    assert n>0,"Fruit distribution must be given a positive integer. Given: {}".format(n)

    
    orange_apples = s.split(" ")
    assert len(orange_apples)==2,"Orange and apple distribution must contain two items. Given: {}".format(s)

    assert int(orange_apples[0])+int(orange_apples[1]) == n,"Total number of oranges and apples does not equal the number of fruits in the basket. Given: {}".format(s)
    assert int(orange_apples[0])>0,"Number of oranges cannot be negative. Given: {}".format(s)
    assert int(orange_apples[1])>0,"Number of apples cannot be negative. Given: {}".format(s)

    orange,apples = orange_apples
    orange = int(orange)
    apples = int(apples)

    mango = n-orange-apples

    return mango
