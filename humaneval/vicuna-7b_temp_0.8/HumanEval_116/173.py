
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
    # Here we have a function that takes in an array of integers and returns a new array of integers
    # The function uses two nested loops to iterate through the elements of the input array
    # It will check for a carry flag and use it to swap values between adjacent bits
    # In this way, the function will sort the array in a way that the most significant bit
    # is always a 1.

    def count_ones(arr):
        # Here we count the number of ones in the binary representation of each element
        ones = 0
        for x in arr:
            if x > 0:
                ones += (x & (x - 1))
        return ones

    arr = list(arr)
    sorted_arr = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # If there is a carry from the previous iteration, it means that the current element is greater
            # than the sum of the previous elements. In this case, we swap the current element with
            # the last element and increment the count of ones for the current element.
            if arr[i] > (arr[i - 1] + count_ones(arr[j:])):
                arr[i], arr[j] = arr[j], arr[i]
                ones += (arr[i] & (arr[i] - 1))
                arr[i] = 0
            sorted_arr.append(arr[i])
        arr = [x for x in arr if x != 0]

    return sorted_arr