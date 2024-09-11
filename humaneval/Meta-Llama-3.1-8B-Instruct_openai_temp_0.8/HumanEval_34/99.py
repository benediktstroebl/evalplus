### Unique Elements in a List
#### Python Script
```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Example usage
if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list `l` as input, converts it to a set to remove duplicates, and then sorts the resulting set in ascending order. The `sorted` function returns a new sorted list and leaves the original set unchanged.

The `if __name__ == "__main__":` block is used to ensure that the example usage is only executed when the script is run directly (not when it's imported as a module by another script).