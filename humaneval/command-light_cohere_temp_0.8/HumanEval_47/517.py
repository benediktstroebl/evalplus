```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[(n // 2)]

# Test suite
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 0, median([0, 4, 6])]
    assert lst == [15.0, 6]

test_median()
```
The code defines a function median that calculates the median of the elements in a list. The function first checks if the list has an odd or even amount of elements. Then, it uses the simple formula to calculate the median for the odd-length list and for the even-length list, it takes the middle element as the median.

The code also includes a test suite that creates a list of elements and passes it to the median function. The test suite then compares the expected result with the returned value by the median function.