
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Your code here
    odd_index_elements = []
    even_index_elements = []
    for index, item in enumerate(lst):
        if index % 2 == 0:
            even_index_elements.append(item)
        else:
            odd_index_elements.append(item)
    result = sum(even_index_elements)
    return result

