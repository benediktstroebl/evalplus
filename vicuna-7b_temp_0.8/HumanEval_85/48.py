
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] > 0:
            lst[i], lst[i-2] = lst[i-2], lst[i]
            break

lst = [1, 2, 3, 4, 5, 6, 7, 8]
add(lst)
print(lst)
