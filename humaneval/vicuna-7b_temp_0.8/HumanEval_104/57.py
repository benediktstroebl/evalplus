
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
    # Step 1: sort the list x
    x.sort()
    # Step 2: reverse the list x
    x.reverse()
    # Step 3: iterate through the list x
    for i in range(0, len(x)):
        # Step 4: check the i-th element
        digit = x[i]
        # Step 5: check if the digit is odd
        if digit % 2 == 0:
            # Step 6: add the digit to the list and sort it in the same order
            list1.append(digit)
            list1.sort()
            # Step 7: remove the digit from the list x
            x.remove(digit)
    return list1
