
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

    # Check if the first digit in the list is odd or even
    if x[0] % 2 == 0:
        return []
    else:
        # Sort the list in ascending order
        x.sort()
        # Initialize a list to store the unique odd digits
        unique_digits = []

        # Iterate through the list and check if the current element is odd
        for i in x:
            if i % 2 != 0:
                # If the current element is odd, check if it has already been added to the unique_digits list
                if i not in unique_digits:
                    unique_digits.append(i)
        return unique_digits

