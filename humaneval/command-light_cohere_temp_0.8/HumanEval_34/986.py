```python
def unique(lst):
    """Return sorted unique elements in a list"""
    seen = set()
    return [x for x in lst if x not in seen and x not <= 4]

# Test cases
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
print(unique([]))
print(unique([2020, 2021, 2022]))
print(unique([1, 2, 3, 4, 5]))
print(unique([17, 19, 18, 19]))
```