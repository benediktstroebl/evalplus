Here is a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list as input and returns a list with each element incremented by 1. It uses a list comprehension with a `+ 1` operation to achieve this.