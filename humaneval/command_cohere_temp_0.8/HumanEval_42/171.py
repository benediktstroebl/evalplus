Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and add 1 to it, effectively incrementing each element. The function is self-contained and can easily be imported and used in other scripts.