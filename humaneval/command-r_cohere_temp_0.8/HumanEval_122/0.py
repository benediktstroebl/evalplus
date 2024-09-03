```python
def add_elements(arr, k):
    """
    Return the sum of elements with at most two digits from the first 'k' elements of 'arr'.

    Args:
        arr (list): A non-empty array of integers.
        k (int): An integer specifying the number of elements to consider from the start of the array.

    Returns:
        int: The sum of elements with at most two digits.
    """
    return sum(x for x in arr[:k] if len(str(x)) <= 2)
```