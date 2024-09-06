Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list as input and returns a new list with each element incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

You can use the `incr_list` function in your code to increment the elements of a list by 1. 

This solution is concise and easy to understand, providing a straightforward way to increment list elements by 1. 

You can test this function with sample lists to ensure it performs as expected. Feel free to add test cases to verify different scenarios and ensure the function's correctness. 
```python
# Test incr_list()
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
This confirms that the function correctly increments each element in the list by 1.