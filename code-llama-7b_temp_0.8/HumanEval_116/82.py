
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """

    # these numbers will be the keys to the counts dict
    # for example, 00000100 will be 4
    # count will be a dictionary of the form {4: [1, 2, 3, 4, 5]}
    # for example, {4: [1, 2, 3, 4, 5]}
    count = {}

    # we loop through the array
    for x in arr:

        # convert to binary
        binary_x = bin(x)[2:]

        # get the number of '1's
        ones = binary_x.count('1')

        # if there's no key in count
        if ones not in count:

            # initialize the key as a list
            count[ones] = []

        # append the value to the list
        count[ones].append(x)

    # now we loop through count
    # count = {0: [0], 1: [1], 2: [2, 3], 3: [4]}
    # we need to keep a running total of the number of times we've seen a value
    # in order to maintain the order
    # for example, 0 will be 0, 1 will be 1, 2 will be 2, 3 will be 3, 4 will be 4
    total = 0

    # the resulting list
    result = []

    # we loop through count
    for key in sorted(count.keys()):

        # we need to loop through the list in count[key]
        # for example, for key = 1, count[1] = [1]
        # for example, for key = 2, count[2] = [2, 3]
        # we need to loop through [2, 3]
        for value in count[key]:

            # we add the running total to each item in count[key]
            result.append(value)
            result.append(total)

            # for example, the first time through the loop, the running total
            # would be 1. The first item in count[1] would be 1. After the
