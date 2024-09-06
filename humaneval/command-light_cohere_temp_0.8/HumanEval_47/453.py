```python
def median(l):
    # Sort the list
    l.sort(l)
    # Return the median of the two middle numbers in the sorted list
    m1, m2 = l[(len(l) - 1) // 2], l[len(l) // 2]
    return (m1 + m2) / 2

# Test case 1:
assert median([3, 1, 2, 4, 5]) == 3

# Test case 2:
assert median([-10, 4, 6, 1000, 10, 20]) == 15

# Test case 3:
assert median([3, -7, -4, 4, 5]) == 4

# Test case 4:
assert median([2, 2, 8, 6, 6]) == 6

# Test case 5:
assert median([-3, -4, -5, -6]) == -5

# Test case 6:
assert median([1, 2, -3, -4, -5]) == -4
```
This script defines a function `median` that computes the median of the elements in a given list `l`. It sorts the elements in the list, then calculates the median of the two middle numbers in the sorted list. The script also provides several test cases to ensure the correctness of the function. 

This code is a complete program that is self-contained and does not require any external functions or modules.