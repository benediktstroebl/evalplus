```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example use case
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
print(unique([1, 1, 2, 2, 3, 3]))
print(unique([10, 20, 30, 10, 20]))
```

Explanation:
1. We use the built-in Python function `set()` to remove duplicates from the list. However, this function does not preserve the original order of elements.
2. To get the unique elements in the original order, we would need to convert the list to a dictionary where the keys are the elements and the values are all `None`. Then we would convert the dictionary keys back to a list and sort it.
3. We use `sorted()` function to sort the unique elements in ascending order.

In this solution, we directly use the `set()` function to remove duplicates and then sort the resulting set. This approach is more concise and efficient than the alternative method that involves converting the list to a dictionary.