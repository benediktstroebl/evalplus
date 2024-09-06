
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum(lst[::2])

assert add([4, 2, 6, 7]) == 2, "test 1 failed"
assert add([4, 2, 7]) == 5, "test 2 failed"
assert add([5]) == 5, "test 3 failed"
assert add([5, 8, 10, 3]) == 12, "test 4 failed"
assert add([5, 8, 10, 3, -10]) == 10, "test 5 failed"

