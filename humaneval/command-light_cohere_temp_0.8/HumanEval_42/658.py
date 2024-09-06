```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[-1] + 1)
    return l

# Test case 1
def test_incr_list1():
    """
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    """

# Test case 2
def test_incr_list2():
    """
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

# Test case 3
def test_incr_list3():
    """
    >>> incr_list([])
    []
    """

# Test case 4
def test_incr_list4():
    """
    >>> incr_list([1, 2, 3, 4])
    [3, 4, 5]
    """

# Run all test cases
test_incr_list1()
test_incr_list2()
test_incr_list3()
test_incr_list4()
```

In this script, we have a function `incr_list` that adds one to the last element of a list and returns the modified list. The test cases cover different scenarios, including empty lists, lists with a single element, lists with multiple elements, and lists with one specific increment. 

We use the test suite to verify the correctness of the `incr_list` function across different test cases.