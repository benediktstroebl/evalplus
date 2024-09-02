
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
    if arr is None or len(arr) == 0:
        return arr

    # num of bits in int64
    bits = 64

    # Initialize buckets for each number of 1's
    buckets = [[] for _ in range(bits)]
    max_val = 0

    # Put each number in the correct bucket
    for num in arr:
        # To count number of 1's, need to convert to binary string
        # Can use num.to_bytes to get the binary representation
        # The default length for to_bytes is 8, so need to get just the first 8
        # Chars for this
        bin_str = f'{num:b}'.zfill(bits)
        num_ones = bin_str.count("1")

        # Put number in the correct bucket
        buckets[num_ones].append(num)

        # Keep track of maximum number of 1's
        max_val = max(max_val, num_ones)

    # Sort each bucket
    for bucket_idx in range(max_val + 1):
        buckets[bucket_idx].sort()

    # Now put numbers in the array
    sorted_arr = []
    for bucket_idx in range(max_val + 1):
        sorted_arr.extend(buckets[bucket_idx])

    return sorted_arr

