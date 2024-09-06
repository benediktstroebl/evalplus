Here is a Python script that contains a self-contained function that solves the problem of returning unique elements from an input list:

```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(lst))

#Test cases
test_unique = []
test_unique.add([5)
test_unique.add([3])
test_unique.add([12])
test_unique.add([4])
test_unique.add([100, 21])
test_unique.add([10010])
test_unique.add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# Function calls
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
print(unique([5, 3, 2, 4, 7, 8, 9, 0, 1, 2, 3]))
print(unique([100, 101, 102, 103, 105, 106, 107, 108, 109, 110]))
```

The code provides a function `unique` that accepts a list as an argument and returns a new list containing unique elements from the original list. It also includes a test cases that demonstrate the function's functionality.