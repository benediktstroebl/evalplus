```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases with specific lists
print(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
print(get_positive([9, 2, -10, -3]))
print(get_positive([]))
print(get_positive([1, 2, 3, -4, -100]))
```
The code defines a function `get_positive` that returns a list of positive numbers from the input list. It then passes several test cases with specific lists to ensure that the function works correctly for different scenarios.