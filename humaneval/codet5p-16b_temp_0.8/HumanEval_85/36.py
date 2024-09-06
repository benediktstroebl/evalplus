
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    even = []
    odd = []
    for i in range(len(lst)):
        if i % 2 == 0:
            even.append(lst[i])
    for i in range(len(lst)):
        if i % 2!= 0:
            odd.append(lst[i])
    return sum(even) - sum(odd) 

