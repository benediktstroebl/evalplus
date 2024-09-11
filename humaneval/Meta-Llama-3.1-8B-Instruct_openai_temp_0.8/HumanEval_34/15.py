```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Explanation:

1.  We define a function `unique` that takes a list `l` as input.
2.  The function uses the built-in `set` function to remove duplicates from the list. Since sets only store unique elements, this operation effectively removes duplicates.
3.  We then use the `sorted` function to sort the unique elements in ascending order.
4.  The sorted unique elements are returned as the result of the function.
5.  In the example usage, we call the `unique` function with a list that contains duplicate elements and print the result.