```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# test cases
test_median = lambda: median([3, 1, 2, 4, 5]) == 3.0
test_median_even = median([-10, 4, 6, 1000, 10, 20]) == 15.0
test_median_odd = median([-1000, 4, 6, 10, 20]) == 1000.0

if test_median() and test_median_even() and test_median_odd():
    print("All test cases passed!")
else:
    print("Test cases failed.")
```