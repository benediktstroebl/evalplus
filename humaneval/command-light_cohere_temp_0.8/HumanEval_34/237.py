Here's the solution:

```python
def unique(l: list):
    seen = set()
    result = []
    for num in l:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

This function `unique` accepts a list `l` and returns a new list containing only the unique elements from the input list. It uses a method `set()` to create a set of unique elements and then loops through the input list, adding elements to the set and to the `result` list if they are not already present in the set. This ensures that all element is unique and returns the `result` list.