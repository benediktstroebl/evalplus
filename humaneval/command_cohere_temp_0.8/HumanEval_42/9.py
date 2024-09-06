Here is a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list `l` as input and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. 

To test this function, you can run the following code, prompting the behavior expected in the problem statement: 
```python
# Test incr_list function
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This demonstrates that the `incr_list` function correctly increments each element of the input list by 1, producing the expected output.