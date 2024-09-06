```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    m = 0
    for x in lst:
        m += x
    m = (m + lst[len(lst)//2]) / 2
    return m
# Test cases
median([-10, 4, 6, 1000, 10, 20]) # Should return 15.0
median([1, 2, 3, 4]) # Should return 2.0
median([-20, -10, -15]) # Should return -15.0
median([20, 10, 40]) # Should return 10.0
```
The code defines a median function that computes the median of a list of numbers. It first checks if the basic cases, then it iterates through the list and maintains a running sum. After adding up to the half of the sum, it computes the average and returns the result.