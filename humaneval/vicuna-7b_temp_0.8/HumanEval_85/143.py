
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Check if list is empty
    if not lst:
        return []

    # Check if list is odd
    if len(lst) % 2 == 1:
        # Add the even element at odd indices
        return lst[0] + lst[1]
    else:
        # If the list is even
        even_lst = []
        odd_lst = lst[:]
        while odd_lst:
            odd_lst.append(odd_lst.pop(0))
            even_lst.append(even_lst.pop(0))
        return even_lst[0] + odd_lst[0] + even_lst[-1]
