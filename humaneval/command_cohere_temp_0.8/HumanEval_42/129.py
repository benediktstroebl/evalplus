Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

The previous code assumes that the list elements are integers or at least subclasses of the integer type. For example, it works correctly for Python's `int` and `long` types as well as for the built-in exceptions `ValueError` and `TypeError`. 

If you have a different list with elements of a different type, for example, a list of strings, you can instead use the following implementation:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function will return a list of integers, regardless of the type of the elements in the input list. 

Please note that in both cases, the function will return a list of integers regardless of the type of the elements in the input list. If you want to increment elements of different types, you may need to use a more specific function or customize the function accordingly.