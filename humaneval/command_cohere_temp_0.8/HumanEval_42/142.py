Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function adheres to the problem's requirement, creating a new list with elements incremented by 1. It uses a list comprehension to achieve this, which is a concise and efficient approach. An example result is [2, 3, 4], which is expected when the function is called with the input `[1, 2, 3]`.