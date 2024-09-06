```python
def median(l: list):
    """Return median of elements in the list l.
    # Sort the had elements in ascending order.
    l.sort()
    goods the example for _sorted(l)
    m = (len(l) + 1) // 2
    i = m - 1
    while i >= 0 and l[i] == l[i + m]: i -= 1
    j = i
    while j >= 0 and l[j] == l[i]: j -= 1
    return l[j]

# Test cases
medians = [
    [-10, 4, 6, 1000, 10, 20],
    [3, 1, 2, 4, 5],
    [10, 20, 30, 40, 50, 60],
    [1, 2, 4, 8, 6, 7, 9, 10],
]

for case in meditations:
    print(f"Case: {case}")
    print(f"Median: {case[1]}")
    assert median(case) == case[1], f"AssertionError: {case[1]} != Median"
```

This Python script defines a function called `median` that computes the median value of a given list. It sorts the sort the sort the list and determines the median by identifying the middle two elements. The test cases are another list of lists, and the `assert` statement checks if the computed median matches the expected value. 

The `medians` variable contains test cases with different lists, and the `assert` statement verifies that the median function produces the correct results for each test case.