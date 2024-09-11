```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This scripts defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then returns a sorted list of unique elements. The `if __name__ == "__main__"` block is used to ensure that the `unique` function is only called when the script is run directly (not when it's imported as a module).