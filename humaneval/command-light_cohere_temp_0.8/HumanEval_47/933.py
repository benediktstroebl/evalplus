```python
def median(l):
    """Return median of elements in the list l."""
    # Sort the list in ascending order
    l.sort()
   
    return sorted(l)[len(l) // 2]

# Test case 1
def test1():
    assert median([3, 1, 2, 4, 5]) == 3

# Test case 2
def test2():
    assert median([-10, 4, 6, 1000, 10, 20]) == 5.0

# Test case 3
def test3():
    assert median([1, 2, 4, 5, 6]) == 4.0

# Test case 4
def test4():
    assert median([-20, -15, -10, 4, 6, 8, 9]) == 5.0

# Test case 5
def test5():
    assert median([10, 20, 30, 40, 25]) == 30.0

# Test case 6
def test6():
    assert median([100, 200, 150, 60, 30]) == 75.0

test1()()
test2()
test3()
test4()
test5()
test6()
```

This script defines a function `median` that computes the median of a list of numbers. The test cases are also included, passing the function with various test lists.  The code is self-contained, and only requires the function median to be called. 

The median is the value that divides a list of numbers into two equal parts and is often used in statistics and data analysis.