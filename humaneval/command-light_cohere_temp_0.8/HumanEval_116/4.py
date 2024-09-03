```python
def sort_array(arr):
    """
    Sorts an array of integers (non-negative) based on the number of ones in their binary representation.
    Returns an sorted array in ascending order.

    Test suite:
    >>> arr = [1, 5, 2, 3, 4]
    >>> sort_array(arr) == [1, 2, 3, 4, 5]
    >>> arr = [-2, -3, -4, -5, -6]
    >>> sort_array(arr) == [-6, -5, -4, -3, -2]
    >>> arr = [1, 0, 2, 3, 4]
    >>> sort_array(arr) == [0, 1, 2, 3, 4]
    """
    arr.count_ones = 0
    binary_count = 0
    for num in arr:
        binary_count += bin(num).count_ones = count_ones
        arr.count_ones += 1
        number_ones = binary_count // 2
        arr.binary_str = ''.join(binary_count, 'b')
        arr = [int(num) for num in arr_binary_str.split()]
    other words,
    arr = sorted(arr)
    return arr
```