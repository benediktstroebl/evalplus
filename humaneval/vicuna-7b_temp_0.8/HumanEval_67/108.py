
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
    n1 = n % 10
    n = n // 10
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 4
    if n == 5:
        return 5
    if n == 6:
        return 6
    if n == 7:
        return 7
    if n == 8:
        return 8
    if n == 9:
        return 9
    if n1 == 1:
        return int(s[0])
    if n1 == 2:
        return int(s[0]) + int(s[1])
    if n1 == 3:
        return int(s[2]) + int(s[3]) + int(s[4])
    if n1 == 4:
        return int(s[5]) + int(s[6]) + int(s[7]) + int(s[8])
    if n1 == 5:
        return int(s[9]) + int(s[10]) + int(s[11]) + int(s[12]) + int(s[13])
    if n1 == 6:
        return int(s[14]) + int(s[15]) + int(s[16]) + int(s[17]) + int(s[18]) + int(s[19])
    if n1 == 7:
        return int(s[20]) + int(s[21]) + int(s[22]) + int(s[23]) + int(s[24]) + int(s[25]) + int(s[26]) + int(s[27]) + int(s[28]) + int(s[29]) + int(s[30])
    if n1 == 8:
        return int(s[31]) + int(s[32]) + int(s[33]) + int(s[34
