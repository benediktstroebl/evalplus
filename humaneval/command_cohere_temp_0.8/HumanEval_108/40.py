```python
def count_nums(arr):
    return sum(int(b) for a in arr for b in str(a) if b != '0')
```