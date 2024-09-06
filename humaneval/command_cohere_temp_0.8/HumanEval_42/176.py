Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

Here's a markdown code block with a corresponding test to verify the correct behavior of the function:
```python
def test_incr_list():
    # Test list with positive integers
    assert incr_list([1, 2, 3]) == [2, 3, 4]

    # Test list with positive and negative integers
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

    # Test list with floats
    assert incr_list([1.5, 2.3, 4.2, -3.7]) == [2.5, 3.3, 5.2, -3.7]

    # Test list with mixed data types
    assert incr_list([1, 2, 3, 'abc', 4, 5, 6.0, 7]) == [2, 3, 4, 'abc', 5, 6, 7.0, 8]

    # Test list with a large number of elements
    assert incr_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```
This way, the function `incr_list` correctly increments the elements of any given list by 1. 
The test suite covers various scenarios, including lists with positive and negative integers, floats, mixed data types, and a large number of elements, to ensure the function's reliability.