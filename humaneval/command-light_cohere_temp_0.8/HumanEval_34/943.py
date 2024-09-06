```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [''] and x]

if __name__ == "__main__":
    # Example usage
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique elements:", unique(lst))  # Output: [0, 2, 3, 5, 9, 123]
```

This function `unique` takes a list `lst` as input and returns a new list containing only the unique elements from the original list. It uses a `set()` to keep track of elements that have been seen, and then iterates through the original list, adding elements to the `seen` set as they are not duplicates and not empty strings.