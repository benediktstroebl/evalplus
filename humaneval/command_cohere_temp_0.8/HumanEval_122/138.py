Here's a Python script that includes a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = sum(el for el in arr[:k] if len(str(el)) <= 2)
    return sum_two_digits
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:
        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
```
This script provides a function that takes an array `arr` and an integer `k` as input, and returns the sum of elements in `arr` that have at most two digits when converted to strings. The function does this by using a generator expression within the `sum` function to filter the relevant elements from the first `k` elements of the array.

Note that this code assumes that the given constraints are satisfied. If the input array has more than 100 elements or if `k` is larger than the length of the array, the function will still work but may lead to incorrect results.