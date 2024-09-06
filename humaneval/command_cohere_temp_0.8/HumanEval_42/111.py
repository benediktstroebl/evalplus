Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function adheres to the problem's specification, returning a list where each element is incremented by 1. It utilizes a list comprehension to iterate over each element in the input list and compute the incrementation. The output is a new list comprising the incremented elements.