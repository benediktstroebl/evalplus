
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:
        return []
    n = len(array)
    if n == 1:
        return array[0]
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    left[0] = array[0]
    for i in range(1, n):
        if i == 0:
            left[i] = array[i]
        else:
            right[i] = array[i]
    while left and right:
        while left[0] <= right[0] and (left[0] % 2 == 0 or (left[0] - right[0]) % 2 == 0):
            left[0] += 1
            if left[0] == right[0]:
                break
        while left[0] <= right[0] and (left[0] % 2 == 0 or (left[0] - right[0]) % 2 == 0):
            right[0] -= 1
            if left[0] == right[0]:
                break
        if left[0] > right[0] and (left[0] % 2 == 0 or (left[0] - right[0]) % 2 == 0):
            return []
        left, right = right, left[1:]
    if left:
        return left + right

solution = sort_array(numbers)
