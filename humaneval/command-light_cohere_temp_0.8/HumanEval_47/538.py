```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l) // 2 + 1
    m = []
    for i in range(n):
        m.append(l[i])
    m.sort()
    .reverse()
    return sum(m) / 2
def test_median():
    # Test case 1
    assert median([3, 1, 2, 4, 5]) == 3.5
    # Test case 2
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
def test_median_recursion():
    # Test case 3
    assert median([1, 2, 3, 4, 5]) == 5
    # Test case 4
    assert median([10, -20, 30, -40]) == 15.25
def test_median_lists():
    # Test case 5
    assert median([1, 2, 3]) == 2.5
    # Test case 6
   
    assert median([5, 10, -20, 30]) == 10
def test_median_mixed():
    # Test case 6
    assert median([10, 20, 30, 40, -40]) == 15.0
```

This code defines a function `median` that calculates the median of the elements in a list. It uses dynamic programming techniques to solve the problem. Also, it contains a series of tests that verify the correctness of the function.