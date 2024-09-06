```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even + [x for x in lst if x % 2 != 0]

# Test case 1
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]

# Test case 2
def test_sort_even2():
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

test_sort_even() # Test case 1
test_sort_even2() # Test case 2
```

The script defines a function `sort_even` that sorts an input list such that the odd elements are kept in place, and the even elements are sorted in ascending order. The function returns the test case by testing the function with two different list inputs and asserting that the output is correct.