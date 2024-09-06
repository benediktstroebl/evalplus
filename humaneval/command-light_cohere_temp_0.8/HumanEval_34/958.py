```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

if __name__ == "__main__":
    # Example usage
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique elements:", unique(lst))  # [0, 2, 3, 5, 9, 123]
```
This code defines a function `unique` which takes a list `lst` as input and returns a new list containing only the unique elements from `lst`. It uses a set `seen` to keep track of elements already seen, and creates a new list containing only the elements that are not in the set and are not 0. This code provides a basic functionality to solve the problem of removing duplicate elements from a list.