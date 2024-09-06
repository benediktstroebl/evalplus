
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
    # create a list with same number of element as arr
    sorted_arr = [None] * len(arr)
    # resultant array to be sorted
    resultant_arr = []

    # sorting by count of ones
    for i in range(len(arr)):
        # count the number of ones in binary representation
        num_ones = 0
        while arr[i] > 0:
            if arr[i] % 2 == 1:
                num_ones += 1
            arr[i] = arr[i] // 2
        # append the sorted value to the array
        resultant_arr.append(num_ones)

    # bubble sort
    for i in range(len(resultant_arr)):
        for j in range(len(resultant_arr) - 1):
            if resultant_arr[j] > resultant_arr[j + 1]:
                resultant_arr[j], resultant_arr[j + 1] = resultant_arr[j + 1], resultant_arr[j]

    # append the values to sorted_arr
    for i in range(len(resultant_arr)):
        for j in range(len(arr)):
            if resultant_arr[i] == num_ones(arr[j]):
                sorted_arr[i] = arr[j]

    return sorted_arr

