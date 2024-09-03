```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# test function to check the correctness of median function
def test_median():
    # list with odd and even elements
    lst = [-10, 4, 6, 1000, 10, 20, -5, 2, 8]
    assert median(lst) == 2
# test list with all odd elements
    lst = [-10, -5, -9, -13, -15]
    assert median(lst) == -5
# test list with all even elements
    lst = [2, 4, 6, 8, 10, 12, 14]
    assert median(lst) == 6
# random list to test median function
    lst = [3, 2, 8, 1, 7, 5, 9, 6]
    assert median(lst) == 5
```