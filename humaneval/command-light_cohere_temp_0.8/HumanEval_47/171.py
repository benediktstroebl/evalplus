```python
def median(lst):
    n = len(lst) // 2 + 1
    mid = n // 2
    if lst[mid] > lst[mid - 1]:
        mid += 1
    return (lst[mid] + lst[mid - 1]) / 2
# Test case 1
if median([-10, 4, 6, 1000, 10, 20]) != 15.0:
    raise Exception("Function failed test case 1.")

# Test case 2
lst2 = [-200, 0, 400, 200]
if median(lst2) != 314.0:
    raise Exception("Function failed test case 2.")

# Test case 3
lst3 = [1, 2, 3, 4, 5, 6]
if median(lst3) != 3.0:
    raise Exception("Function failed test case 3.")
```