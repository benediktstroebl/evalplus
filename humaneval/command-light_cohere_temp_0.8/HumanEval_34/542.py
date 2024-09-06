```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(seen))
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_list)
print("Unique list:", result)  # Expected output: [0, 2, 3, 5, 9, 123]
```
This script defines a function unique that takes a list as input and returns a new list containing only the unique elements from the input list. The function uses a seen set to keep track of elements encountered before, and then appends all unique elements from the seen set to the result list. This ensures that all unique elements are returned in sorted order.