
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_list = []
    for num in range(len(lst)):
        if lst[num] % 2 == 0 and num % 2 == 1:
            even_list.append(lst[num])
    return sum(even_list)
