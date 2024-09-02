
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    left, right = 0, 1
    while left < len(lst)-1:
        if lst[left] % 2 == 0:
            right += 1
        left += 1
    return lst[left], lst[right]

lst = [1, 2, 3, 4, 5, 6]
