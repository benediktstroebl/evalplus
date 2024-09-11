```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = set()
    result = []
    for elem in l:
        if elem not in seen:
            seen.add(elem)
            result.append(elem)
    return sorted(result)


if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates, and returns a sorted list of unique elements. It uses a set to keep track of elements that have been seen and a list to store the result. The `sorted` function is then used to sort the result in ascending order. The script includes a test case in the docstring and demonstrates the usage of the `unique` function in the `if __name__ == "__main__":` block.