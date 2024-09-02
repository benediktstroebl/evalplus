
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_list = [num for index, num in enumerate(lst) if not index % 2]
    sum = 0
    for num in even_list:
        sum += num
    return sum

