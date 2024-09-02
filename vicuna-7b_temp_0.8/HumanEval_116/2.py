
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
    # sort the array
    sorted_array = sorted(arr)

    # reverse the array
    reversed_array = [arr[0], arr[1], arr[2], arr[3], arr[4]]

    # initialize the count of 1s and the sum of the elements
    count_of_1s = 0
    sum_of_elements = 0

    # traverse the array
    for i in range(len(sorted_array)):
        # count the number of 1s
        count_of_1s += sorted_array[i]
        # add the current element to the sum of elements
        sum_of_elements += sorted_array[i]

        # if the number of 1s is greater, update the count and sum
        if count_of_1s > sum_of_elements // 2:
            count_of_1s = sum_of_elements // 2
            sum_of_elements = sorted_array[i]

    # reverse the array again
    reversed_array[0] = sum_of_elements
    reversed_array[1] = count_of_1s

    return reversed_array
