
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
    return s.count('A') * n + s.count('B') * n + s.count('C') * n + s.count('D') * n + s.count('E') * n + s.count('F') * n + s.count('G') * n + s.count('H') * n + s.count('I') * n + s.count('J') * n + s.count('K') * n + s.count('L') * n + s.count('M') * n + s.count('N') * n + s.count('O') * n + s.count('P') * n + s.count('Q') * n + s.count('R') * n + s.count('S') * n + s.count('T')
