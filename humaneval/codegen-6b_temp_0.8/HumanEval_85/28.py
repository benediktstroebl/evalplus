
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if len(lst) == 0:
        return 0

    i = 0
    for i in range(0, len(lst), 2):
        lst[i] += lst[i + 1]
        lst.pop(i + 1)

    return lst[0]


assert add([1, 2, 3, 4]) == 2
assert add([10, 4, 5]) == 5

