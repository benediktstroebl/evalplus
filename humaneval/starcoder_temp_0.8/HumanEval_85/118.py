
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_indices = [n for n in range(0, len(lst), 2)]
    return sum([lst[n] for n in even_indices if n % 2!= 0])
