
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    temp = []
    for i in lst:
        if i % 2 == 0:
            temp.append(i)
    lst[0] += sum(temp) # sum is only integer add
    del lst[1:]


