
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
    n=1
    mango=0
    word=[]
    for i in s:
        if i=='a':
            n+=1
        elif i=='o':
            n+=1
        elif i=='m':
            mango+=1
        else:
            continue
    return n*2+mango
    # if s=='':
    #     print("Please write the number of fruits first")
    # elif s[0]=='a' or s[0]=='o' or s[0]=='m':
    #     print(s)
    #     for i in s:
    #         if i=='a':
    #             n+=1
    #         elif i=='o':
    #             n+=1
    #         elif i=='m':
    #             mango+=1
    #         else:
    #             continue
    #     return n*2+mango
    # else:
    #     print("Invalid input")
