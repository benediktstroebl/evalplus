
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
    # Return an empty list if the list is empty
    if not x:
        return []

    # Create an empty set to store the unique digits
    unique_digits = set()

    # Loop through each element in the list
    for element in x:
        # Convert the element to a string
        str_element = str(element)

        # Loop through each digit in the string
        for digit in str_element:
            # If the digit is even, skip it
            if int(digit) % 2 == 0:
                continue

            # If the digit is unique, add it to the set
            if int(digit) not in unique_digits:
                unique_digits.add(int(digit))

    # Create a new list to store the sorted unique digits
    unique_digits_list = list(unique_digits)

    # Sort the list in increasing order
    unique_digits_list.sort()

    # Return the sorted list
    return unique_digits_list
