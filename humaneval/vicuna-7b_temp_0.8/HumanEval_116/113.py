
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
    def count_ones(arr):
        """Count number of ones in an array"""
        return sum(1 for x in arr if x > 0)

    def binary_to_decimal(x):
        """Convert binary to decimal"""
        return (x + (x >> 1)) >> 1

    arr = sorted(arr, key=count_ones)
    arr = sorted(arr, key=binary_to_decimal)
    return arr

test_cases = [
    [1, 5, 2, 3, 4],
    [-2, -3, -4, -5, -6],
    [1, 0, 2, 3, 4],
]

for test_case in test_cases:
    print("Test case:", test_case)
    result = sort_array(test_case)
    print("Expected result:", test_case)
    print("Sorted array:", result)
    assert result == test_case, f"{result} != {test_case}"