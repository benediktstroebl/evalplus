
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
    # 1st pass - determine if its possible to make it palindromic
    # 2nd pass - determine the smallest number of elements that need to be changed

    # hashmap from number to frequency
    freq_map = {}

    # iterate through array
    # for each element in array
    # 	if its not in the map, set its frequency to 1
    # 	if its in the map, increment its frequency

    for el in arr:
        if el not in freq_map:
            freq_map[el] = 1
        else:
            freq_map[el] += 1

    # check to see if there are an odd number of elements
    # if so, return the number of all elements
    # if not, return the number of odd elements

    return min(freq_map.values()) - max(freq_map.values()) // 2
