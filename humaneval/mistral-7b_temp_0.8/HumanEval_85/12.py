
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_values = []
    odd_indexes = []
    for index, value in enumerate(lst):
        if value % 2 == 0:
            even_values.append(value)
        if index % 2 != 0:
            odd_indexes.append(index)

    return sum(even_values[odd_indexes])

