
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
    # Use a dictionary to count the number of 1's in each number
    num_ones = defaultdict(int)
    for x in arr:
        num_ones[x] += 1

    # Sort the dictionary
    num_ones_key = lambda x: x + '0'
    num_ones.sort(key=num_ones_key, reverse=True)

    # Reverse the array to preserve the order of the sorted dictionary
    arr = [num_ones[num] for num in arr]

    return arr