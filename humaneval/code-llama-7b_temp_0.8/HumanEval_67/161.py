
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
    # your code here
    apples, oranges, total = 0, 0, 0
    apples_str = "apples"
    oranges_str = "oranges"
    apples_pos = s.find(apples_str)
    oranges_pos = s.find(oranges_str)

    if apples_pos != -1:
        s_apples = s[apples_pos+6:apples_pos+7]
        if s_apples.isnumeric():
            apples = int(s_apples)
        else:
            apples_pos = apples_pos + 1
            s_apples = s[apples_pos:apples_pos+1]
            if s_apples.isnumeric():
                apples = int(s_apples)
            else:
                apples = 0

    if oranges_pos != -1:
        s_oranges = s[oranges_pos+8:oranges_pos+9]
        if s_oranges.isnumeric():
            oranges = int(s_oranges)
        else:
            oranges_pos = oranges_pos + 1
            s_oranges = s[oranges_pos:oranges_pos+1]
            if s_oranges.isnumeric():
                oranges = int(s_oranges)
            else:
                oranges = 0

    total = n - apples - oranges
    return total
