```python
def count_nums(arr):
    """
    Count elements with a sum of digits > 0.
    """
    return sum(1 for num in arr if sum(int(dig) for dig in str(abs(num))) > 0)
```