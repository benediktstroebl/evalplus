
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
    unique_list = []
    # loop through the list to check if any digit is not even
    for element in x:
        # string of number
        string_element = str(element)
        # bool to check if has even digit
        is_even = False
        # loop through the digits of the element to check if there are even digits
        for digit in string_element:
            if int(digit) % 2 == 0:
                # if the digit is even, change the bool to true and break out of the loop
                is_even = True
                break
        if not is_even:
            # if the bool is not changed, add element to the unique_list
            unique_list.append(element)
    # sort the list
    return sorted(unique_list)


