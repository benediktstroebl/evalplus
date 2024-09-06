def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Convert list to set to filter out even digits
    elements = set(x)
    even_digit = '[02468]'
    filtered_elements = {elem for elem in elements if not any(char in even_digit for char in str(elem))}
    return sorted(filtered_elements)