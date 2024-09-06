Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. 

To follow the problem statement, we should also include some test cases to verify the function behavior:
```python
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
>>> incr_list([0, 5, 6, 7, 8])
[1, 6, 7, 8, 9]
>>> incr_list([-5, -4, -3, -2, -1])
[{-4, -3, -2, -1, 0}]
```
This script will yield the expected results as described in the problem statement. Feel free to add more test cases to cover different scenarios and ensure the function is working correctly. 
If you want to refine the tests according to specific scenarios, let me know, and we can work on that together.