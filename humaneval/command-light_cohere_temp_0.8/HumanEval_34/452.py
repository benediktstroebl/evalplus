```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(seen))
    return result

# Test the function
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)
```
This code defines a function named `unique` that takes a list `lst` as input and returns a new list containing unique elements from the original list. The function uses a set called `seen` to keep track of elements that have been encountered so far. Then, it iterates through the list, and for each element, it checks if it's already in the `seen` set. If it's unique, it's added to the `result` list and the `seen` set. Finally, the `result` list contains the unique elements and the function returns this list.