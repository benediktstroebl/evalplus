```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[(n-1) // 2] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test the median function
test_lst = [10, 20, 35, 7, 12, 23]
test_result = median(test_lst)
assert test_result == 15.0

# Test passing odd length list
odd_lst = [10, 20, 35, 7]
test_result = median(odd_lst)
assert test_result == 35
```