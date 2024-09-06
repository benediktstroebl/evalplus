Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to iterate over each element in the input list and increment it by 1. The incremented values are then returned in a new list.

To verify the correctness of the function, two test cases are provided:
```python
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The output shows that the function correctly increments each element in the input lists, thereby confirming the expected behavior of the `incr_list` function.