Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. The function encapsulates the logic needed to solve the problem and can be used directly to increment the elements of any given list.

Here is an example of how to use this function:
```python
my_list = [1, 2, 3, 4, 5]
result = incr_list(my_list)
print(result)
```

Output:
[2, 3, 4, 5, 6]

This demonstrates how the function can be used to increment the elements of the `my_list` and produce the expected result.