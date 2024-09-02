
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
    # create a list of all the elements in the list
    nums = [x for x in x]

    # convert all the digits to integers
    nums = [int(n) for n in nums]

    # create a dictionary to count the number of occurrences of each digit
    num_dict = {}
    for num in nums:
        for i in range(len(str(num))):
            if num_dict.get(str(num)[i], 0) < 2:
                num_dict[str(num)[i]] += 1
    #sort the dictionary in descending order
    num_dict_sort = sorted(num_dict.items(), key=lambda x: -x[1], reverse=True)

    #create a list to store the unique digits
    unique_digits = []
    for key in num_dict_sort:
        if not num_dict_sort[key] % 2 == 0:
            unique_digits.append(key)

    return unique_digits
