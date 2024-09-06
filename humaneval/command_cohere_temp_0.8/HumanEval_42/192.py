Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to iterate over each element in the input list and increment it by 1. The incremented values are then returned in a new list. This solution is concise and efficient, providing a straightforward way to achieve the desired result.

Here is an example of how to use this function:
```python
result = incr_list([1, 2, 3])
print(result)
```
This will print `[2, 3, 4]`, which is the expected output. 

This function can also handle more complex input:
```python
result = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(result)
```
This will print `[6, 4, 6, 3, 4, 4, 10, 1, 124]`.