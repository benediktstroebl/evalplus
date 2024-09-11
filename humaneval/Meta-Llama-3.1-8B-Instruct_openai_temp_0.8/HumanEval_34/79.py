```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(list(set(l)))

# Test the function
if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input, removes duplicates by converting it to a set, and then sorts the elements in ascending order. The `if __name__ == "__main__"` block is a common idiom in Python to ensure that the test code is only executed when the script is run directly, not when it's imported as a module.

When you run this script, it will output:
```
[0, 2, 3, 5, 9, 123]
```