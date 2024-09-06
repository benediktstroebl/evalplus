
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
    def equality(a,b):
        if a == b:
            return True
        else:
            return False

    def counter(s):
        if s[0] == "1":
            num = s[1:]
            return int(num)
        else:
            return int(s)


    def mapper1(x,y):
        if x[0] == "1":
            return (x[1:],y)
        else:
            return (x,y)


    def mapper2(x,y):
        return (x[0],x[1:],y)


    def reducer1(x,y):
        return (x+y)


    def reducer2(x,y):
        return (x,y)


    def mapper3(x):
        return (x,"fruit")


    def reducer3(x,y):
        return (x,y)


    def mapper4(x):
        return (x,"orange")


    def reducer4(x,y):
        return (x,y)


    def mapper5(x):
        return (x,"mango")


    def reducer5(x,y):
        return (x,y)


    def mapper6(x):
        return (x,"apple")


    def reducer6(x,y):
        return (x,y)


    def reversal(x):
        return x[::-1]


    def mapper7(x):
        return (x,x)


    def reducer7(x,y):
        return (x+y)


    def mapper8(x):
        return("mango")


    def reducer8(x,y):
        return(x+y)


    def mapper9(x):
        return("apple")


    def reducer9(x,y):
        return(x+y)


    def mapper10(x):
        return(x,1)


    def reducer10(x,y):
        return(x+y)


    def mapper11(x