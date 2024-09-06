Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

Here's a markdown code block with the above Python code:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function can be tested with the following Python code: 
```python
>> incr_list([1, 2, 3])
[2, 3, 4]
>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The output shows that the function correctly increments the elements in the list.