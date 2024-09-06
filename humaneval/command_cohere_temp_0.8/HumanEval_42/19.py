Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function adheres to the problem's requirement, creating a list result by iterating through the input list l and returning the incremented values by +1. It achieves this using a list comprehension, which facilitates concise explicit mapping. As a result, it fulfills the problem statement's intention of incrementing each element of the input list by 1.