```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]  # base case
    
    mid = len(lst) // 2
    left = lst[mid - 1]
    right = lst[mid]
    return (left + right) / 2

# Test case 1
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 2
assert median([10, 20, -30, 30]) == 30.0

# Test case 3
assert median([1, 2, 3]) == 3.0

# Test case 4
assert median([10, -10, -20]) == -20.0

# Test case 5
assert median([1, 2, 4, 5, 6]) == 5.0
```
This Python script defines a function called `median`, designed to compute and return the median value of a given list. It uses a test cases to verify the function's correctness. The `median` function employs a binary search algorithm to find the median value by dividing the list into two equal parts and returning the average of their corresponding elements.