```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lBound(lst[(n-1)//2], 1) + lBound(lst[(n-1)//2], 2)) / 2
    else:
        return lBound(lst[n//2], 1)

def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

test_median()
```
This Python code defines a function median that calculates the median of a list of numbers. It uses a element-wise average approach for the even-length lists and the last element for the odd-length lists. The test_median function is created to check the correctness of the median function by asserting that it returns the correct result for a given list of numbers.