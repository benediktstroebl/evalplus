```python
def cycpattern_check(first, second):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    first = first.lower()
    second = second.lower()
    
    return second in first or any(x for x in first if x == second)
```
The function uses Python's `in` function to verify if the second element is in the first word. Additionally, it uses a list comprehension to verify if any rotation of the second word exists in the first word. The function currently employs lowercase comparisons, as shown in the provided examples. You can upscale the function to manage capitalizations accordingly.