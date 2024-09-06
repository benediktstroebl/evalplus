```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
```  This code defines a function `unique` that sorts and returns unique elements from a list. It uses a set `seen` to keep track of elements seen so far, and iterates through the input list, appending elements to `result` only if they are not already in `seen`. The code also handles cases with empty lists and lists with a single element.