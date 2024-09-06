
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
    assert isinstance(s,str)
    assert isinstance(n,int)
    assert len(s) == 6
    assert '0' in s
    assert '1' in s
    assert '2' in s
    assert '3' in s 
    assert '5' in s 
    assert '6' in s
    assert '7' in s
    assert '8' in s
    assert '9' in s
    assert '10' in s
    assert '11' in s
    assert '12' in s
    assert '13' in s
    assert '14' in s
    assert '15' in s
    assert '16' in s
    assert '17' in s
    assert '18' in s
    assert '19' in s
    
    assert len(s) == 19
    
    apples = s.count('5')
    oranges = s.count('6')
    mangoes = s.count('7')
    
    apples_in_basket = apples + oranges
    mango_in_basket = mangoes
    all_fruits = apples_in_basket + mango_in_basket
    fruit_left = n - all_fruits
    remaining_apples = apples - apple_left
    remaining_oranges = oranges - orange_left
    remaining_mangoes = mangoes - mango_left
    
    return all_fruits
    
    