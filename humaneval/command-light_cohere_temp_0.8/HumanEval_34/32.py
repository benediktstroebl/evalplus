Here's the Python code to solve your problem:

```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

This function `unique` takes a list `lst` as input and iterates through it. It uses a `set()` to create a set of unique elements, then iterates through the list again and adds elements to `seen` that are also present in the list, but not previously seen. Finally, it returns a list of unique elements from the original list.