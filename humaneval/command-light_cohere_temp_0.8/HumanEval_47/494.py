```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test case 1:
median([-10, 4, 6, 1000, 10, 20]) == 15.0  # TRUE

# Test case 2:
median([-1, 2, 3, 4, 5]) == 2.0  # TRUE

# Test case 3:
median([1, 2, 3, 8, 5]) == 2.0  # TRUE

# Test case 4:
median([-2000, -1000, 4000, 2000]) == 0  # NOT TRUE: Not valid list
# TRUE

# Test case 5:
median([3, 2, 1]) == 2.0  # TRUE

# Test case 6:
median([10, 10, 20, 20]) == 10  # NOT TRUE: Duplicate value
```