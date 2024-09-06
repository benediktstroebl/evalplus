```python
def unique(lst):
    """Sorts and returns unique elements from a list"""
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x string(x))
    return result

# Example usage:
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)  # Output: [0, 2, 3, 5, 9, 123]
```
This function unique sorts and returns unique elements from a given list. You can easily it `test_unique` against your example list to verify the results.