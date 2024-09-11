```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i + 1 for i in l]

# Example usage:
if __name__ == "__main__":
    print(incr_list([1, 2, 3]))  # [2, 3, 4]
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script uses a list comprehension to create a new list where each element is incremented by 1. The `if __name__ == "__main__":` block includes example usage of the function for testing.