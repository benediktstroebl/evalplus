
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # your code here
    #sum1 = 0
    #for i in range(1, len(lst), 2):
        #if lst[i] % 2 == 0:
            #sum1 += lst[i]
    #return sum1
    sum1 = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 != 0:
            sum1 += lst[i]
    return sum1

