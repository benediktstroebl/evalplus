```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        array = sorted(array)
    else:
        array = sorted(array, reverse=True)
    return array
```