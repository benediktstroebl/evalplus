```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result

# Example usage:
# Test with list of numbers
result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Unique elements:", result)
```