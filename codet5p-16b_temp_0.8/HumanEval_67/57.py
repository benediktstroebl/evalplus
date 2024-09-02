
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

    import re
    try:
        if type(n) == int and type(s) == str:
            s_arr = s.split(" ")
            apples_n = int(s_arr[0])
            oranges_n = int(s_arr[1])
            mango_n = apples_n + oranges_n
            if mango_n > 0 and type(mango_n) == int:
                res = re.findall(r"\d+", s)
                if len(res) == 2:
                    print(n - int(res[0]) - int(res[1]))
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
    except:
        print("Error")




