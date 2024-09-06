```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([20]) == []
assert unique([21]) == []
```
This code defines a function `unique` that returns a list containing the unique elements from the input list, after discarding any duplicates and float('inf') values. The test cases demonstrate the after the test the function by asserting that it produces the correct output. This approach uses a unique() function from the built-in library, and the test cases cover various inputs and edge cases.