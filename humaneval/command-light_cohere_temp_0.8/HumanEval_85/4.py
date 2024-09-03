```python
def add(lst):
    """Given a non-empty list of integers lst. add(i) are at odd indices
    Examples:
        add([4, 2, 6, 7]) ==> 2
    """
    i = 3
    sum = 0
    for idx, num in enumerate(lst):
        if idx % 2 == 0:
            sum += num
        i += 1
    return sum
```