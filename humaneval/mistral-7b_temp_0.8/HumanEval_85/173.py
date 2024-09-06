
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_at_odd_indices = []

    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            even_at_odd_indices.append(lst[i])

    return sum(even_at_odd_indices)

