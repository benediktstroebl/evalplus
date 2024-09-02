
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # you can write code here
    n = len(lst)
    sum = 0
    for i in range(0, n):
        if(i%2 != 0):
            sum = sum + lst[i]
    return sum


    # Write your code here


