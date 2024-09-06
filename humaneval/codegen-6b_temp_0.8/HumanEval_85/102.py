
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if lst == []:
        return []
    elif lst[0] % 2 == 0:
        return [lst[0]] + add(lst[1:])
    else:
        return add(lst[1:])

assert add([4, 2, 6, 7]) == [2]
assert add([1, 2, 4, 5]) == [1]
assert add([1]) == [1]
assert add([]) == []
assert add([2, 4]) == [2]









