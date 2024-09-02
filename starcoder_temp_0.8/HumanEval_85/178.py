
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_elements = [value for index, value in enumerate(lst) if index % 2 == 0]
    odd_elements = [value for index, value in enumerate(lst) if index % 2 == 1]
    return sum(even_elements)
