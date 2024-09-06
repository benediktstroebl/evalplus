```python
def incr_list(lst):
    new_elements = [x + 1 for x in lst]
    return new_elements

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3
def test3():
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert l == incr_list(l)
```
This Python code provides a function `incr_list` that adds a value of 1 to each element of a list, effectively incrementing it. The test cases are designed to verify the correctness of the `incr_list` function. The code demonstrates that purpose of the function and provides clear validation for the expected output of the function with different input lists.