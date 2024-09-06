Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to iterate over each element in the input list `l`, incrementing each element by 1. The result is then returned as a new list. This solution has a time complexity of O(n), where n is the length of the input list.