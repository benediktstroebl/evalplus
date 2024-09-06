
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    odd_elements = []
    even_elements = []
    for index, element in enumerate(lst):
        if index % 2 == 1:
            odd_elements.append(element)
        else:
            even_elements.append(element)

    return sum(even_elements)
