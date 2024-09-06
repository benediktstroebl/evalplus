
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
    # sort the input list
    x.sort()
    # initialize a variable to count the number of occurrences of each digit
    digit_count = {digit: 0 for digit in '0123456789'}
    # loop through each element of the input list
    for i in range(len(x)):
        # check if the current element has any even digit
        has_even_digit = False
        for digit in str(x[i]):
            if digit in '0123456789' and digit in digit_count and digit_count[digit] % 2 == 0:
                has_even_digit = True
                break
        # if the element doesn't have any even digit, increment the digit_count
        if not has_even_digit:
            digit_count[str(x[i])] += 1
    # return the sorted list of digit_count
    return sorted(digit_count.items(), key=lambda x: x[1])
