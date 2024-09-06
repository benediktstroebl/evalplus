
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # lst can be empty, so we need to check the length
    if len(lst) == 0:
        return []
    for i in range(len(lst)):
        if i%2 == 1:
            lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

print(add([1,2,3,4,5,6,7,8]))