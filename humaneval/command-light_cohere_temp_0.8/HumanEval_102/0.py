```python
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there are no valid numbers, then the function returns -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    choose_num(5, 10) = 5
    choose_num(10, -8) = -1
    """
    if not x <= y: return -1
    if not y <= x: return -1
    return x + y
```