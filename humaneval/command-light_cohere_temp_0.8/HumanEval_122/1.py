```python
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    :arr: list of integers
    :k: integer

    Returns: sum of elements with at most two digits
    """
    # Include the first element in the sum
    return sum([x for x in arr[:k] if len(str(x)) <= 2])
```

This function takes an array arr and an integer k as input and returns the sum of the elements with at most two digits from the first k elements of the array. It uses a array[:k] to get the first k elements, then uses the condition len(str(x)) <= 2 to check if the current element is less than two digits, and finally returns the sum of all the elements.

This code is self-contained and can be used to solve the problem of adding elements with at most two digits from the first k elements of an given array in a single, efficient function call.