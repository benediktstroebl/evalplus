```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(xq
    unique(result) + [x])
    return result

# Example usage:
# Test passing function
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
# Test obtaining unique elements from list
unique([1, 2, 3, 4, 5])
 ```

This code defines a function `unique` that returns a new list containing only unique elements from the input list. The function uses a set to keep track of seen elements and a list comprehension to filter out duplicate elements, then uses the `append` method to add the unique elements to the result list.