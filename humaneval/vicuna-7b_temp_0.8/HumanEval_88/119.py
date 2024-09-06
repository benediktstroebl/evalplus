
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
    n = len(array)
    if n == 0:
        return []
    elif n == 1:
        return [array[0]]

    # sort the array by the first value
    sorted_array = sorted(array)

    # initialize a variable to store the sum of elements
    running_sum = 0

    # sort the array in descending order if the sum is even,
    # or sort it in ascending order if the sum is odd
    # variable -1 is used to check if the current element is the last element
    # if it's the last element, then we need to check if the running sum is even or odd

    for i in range(1, n):
        # keep track of the running sum
        running_sum += sorted_array[i]

        # check if the running sum is odd or even
        if n % 2 == 0:
            # if the running sum is even, sort the array in descending order
            if running_sum % 2 == 0:
                reversed_array = sorted_array[:i] + [running_sum] + sorted_array[i + 1:]
                return reversed_array
            else:
                reversed_array = sorted_array[:i] + [sorted_array[i]] + sorted_array[:i + 1]
                return reversed_array
        else:
            # if the running sum is odd, sort the array in ascending order
            if running_sum % 2 == 1:
                reversed_array = sorted_array[:i] + [sorted_array[i]] + sorted_array[i + 1:]
                return reversed_array
            else:
                reversed_array = sorted_array[:i] + [running_sum] + sorted_array[i + 1:]
                return reversed_array

    # If we reach this point, we have a single element array,
    # hence we return the same array itself
    return array