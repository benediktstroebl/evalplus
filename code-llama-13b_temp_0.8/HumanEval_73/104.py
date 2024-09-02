
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # for each element in array, store occurences in dictionary
    # if odd, flip next element
    # if even, next 2 elements
    # return number of elements flipped

    # if any element is 0, return 0
    if max(arr) == 0:
        return 0

    # create dictionary for values in arr
    # find max val
    # and create dict
    d = {}
    max_val = max(arr)
    for el in arr:
        if d.get(el) is None:
            d[el] = 1
        else:
            d[el] += 1

    # for each element in dictionary,
    # if val is odd,
    # flip next value
    # if val is even,
    # flip next two values

    # find odd and even values
    odd_values = []
    even_values = []
    for key, val in d.items():
        if val % 2 != 0:
            odd_values.append(key)
        else:
            even_values.append(key)

    # find smallest odd value
    if len(odd_values) != 0:
        smallest_odd = min(odd_values)
        # find next smallest element
        for key, val in d.items():
            if val > 0 and key < smallest_odd:
                next_smallest = key

    # find smallest even value
    if len(even_values) != 0:
        smallest_even = min(even_values)
        # find next smallest element
        for key, val in d.items():
            if val > 0 and key < smallest_even:
                next_smallest = key

    # if odd values, flip next value
    if len(odd_values) != 0:
        # return val - 1
        d[next_smallest] -= 1
        d[smallest_odd] += 1
        return 1
    # if even values, flip next two values
    if len(even_values) != 0:
        # return val - 2
        d[next_smallest] -=
