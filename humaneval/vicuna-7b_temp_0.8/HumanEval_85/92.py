
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i=0
    for num in lst:
        if i % 2 == 1:
            lst[i],lst[lst.index(num)+1] = num,lst[lst.index(num)+1]
            i += 1
    return lst

lst = [1, 2, 3, 4, 5]
