```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_list)
print("Test list:", test_list)
print("Unique elements:", result)
```