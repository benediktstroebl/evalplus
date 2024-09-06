Here's a self-contained Python function that returns the sorted unique elements in a list:
```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Test the function with sample input
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # Output: [0, 2, 3, 5, 9, 123]

# Test the function with another list
another_list = [1, 2, 3, 4, 5, 6, 7]
print(unique(another_list))  # Output: unique([1, 2, 3, 4, 5, 6, 7])
```
This function uses a set to track unique elements, and then appends all the remaining elements (which are not already in the set) to a new list. The result is a list of unique elements.