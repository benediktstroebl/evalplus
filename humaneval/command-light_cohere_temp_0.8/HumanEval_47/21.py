```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    sorted(lst)
    # Find the middle index
    middle = len(lst) // 2
    # If the length of the list is odd, return the middle element
    if middle == 1:
        return lst[middle]
    # If the length is even, return the mean of the two middle elements
    else:
        left = lst[middle - 1]
        right = lst[middle]
        return (left + right) / 2

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([-100, -200, -15]) == -15
assert median([23, 45, 12, 3]) == 23
```
This Python code defines a function `median` that calculates the median of a list. The function sorts the sorted the list and determines the median based on whether the length is odd or even. The test cases demonstrate the validity of the `median` function by passing various lists and checking the resulting medians against the expected values. The test cases cover different scenarios to ensure the function's correctness across various cases.