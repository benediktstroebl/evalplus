Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to iterate over each element in the input list `l`, incrementing each element by 1. The result is then returned as a new list.

You can test this function with the following markdown:
```
```python
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
```
This should result in the same output as the original problem statement. 
The function incr_list successfully completes the task of incrementing the elements in the given list by 1 and returns the modified list. 
If you have any more questions or need assistance with any other coding problems, please let me know!