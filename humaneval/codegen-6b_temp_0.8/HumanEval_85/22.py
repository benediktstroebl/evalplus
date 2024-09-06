
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    sum = 0
    index = 0
    length = len(lst)
    while index < length:
        if index % 2 == 0:
            sum += lst[index]
        index += 1
    return sum


assert add([4, 2, 6, 7]) == 2
assert add([2, 3, 4, 5]) == 5
assert add([2, 2, 6, 7]) == 10
