```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

#Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))
```