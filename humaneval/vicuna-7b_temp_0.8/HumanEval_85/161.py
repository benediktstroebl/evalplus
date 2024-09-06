
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    for i in range(n):
        if i % 2 == 1:
            lst[i] += lst[i+1]
    return lst

print(add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
