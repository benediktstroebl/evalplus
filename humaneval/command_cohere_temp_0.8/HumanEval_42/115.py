Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. 

To test this function, you can run the following code:
```python
Test incr_list():
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This tests the function with two different inputs and checks whether the returned list is correct. 

The `incr_list` function can be modified to perform the increment operation only on elements that are integers. This is demonstrated by the following modified test:
```python
Test incr_list():
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    >>> incr_list([1, 2, 3, 4.5, 5])
    [2, 3, 4, 4.5, 6]
``` 

In this test, the list input includes a mix of numeric and non-numeric elements, and the result is modified to increment only the numeric elements. 
If you want to increment elements based on some other condition, you can modify the list comprehension accordingly. 

Let me know if this solution satisfies the requirement or if there is a specific aspect of the problem that you would like to further discuss!