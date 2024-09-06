```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]
# Uncommented tests
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([]) == 0.0
    assert median([21, 21]) == 21.0
   
test_median()
```
This script defines a function median that computes the median of a list. It then has the test function to verify if the function is working correctly.