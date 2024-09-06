def add(lst):
    """
    Calculates the sum of even integers present at odd indices in the list.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
        add([1, 3, 5, 7, 2, 4, 6]) ==> 12 
    """ 
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)