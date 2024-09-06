
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
    # first pass: count number of ones in each array
    count = defaultdict(int)
    for num in arr:
        for i in range(0, len(num), 2):
            count[num[i]] += num[i+1]

    # second pass: binary sort the counts
    count_list = list(count.items())
    count_list.sort(key=lambda x: x[1] if x[1] != 0 else -1)

    # third pass: convert counts back to numbers and sort the original array
    result = [0] * len(arr[0])
    for i, count in enumerate(count_list):
        for j in range(i, len(arr)):
            result[count] = arr[j]
        arr[i] = result[count]

    return arr