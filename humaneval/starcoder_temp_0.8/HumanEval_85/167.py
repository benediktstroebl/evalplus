
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_at_odd_indices = []
    for index, item in enumerate(lst):
        if index % 2 == 1:
            even_at_odd_indices.append(item)
    return sum(even_at_odd_indices)
