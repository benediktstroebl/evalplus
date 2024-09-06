Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list as input and returns a new list with each element incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, resulting in the output list. The function is self-contained and can easily be copied and pasted into a Python environment to test it out. 

Here's an example of how you can use this function:
```python
# Test the incr_list function
assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The function "incr_list" is tested twice in this example: first with a list of integers [1, 2, 3], and second with a list of integers [5, 3, 5, 2, 3, 3, 9, 0, 123]. The assertions confirm that the function delivers the expected results, providing confidence in its correctness.