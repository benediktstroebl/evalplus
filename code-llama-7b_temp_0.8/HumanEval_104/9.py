
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
    # Your code goes here
    odd_list = []
    for i in x:
        temp = []
        while i > 0:
            num = i % 10
            if num % 2 != 0:
                temp.append(num)
            i = i // 10
        temp_num = 0
        for j in temp:
            temp_num = temp_num * 10 + j
        odd_list.append(temp_num)
    return sorted(odd_list)

