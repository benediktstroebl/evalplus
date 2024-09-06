Here's a self-contained Python function that returns unique elements in a list.

```python
def unique(l: list) -> list:
    seen = set()
    result = []
    for x in l:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result
```

This function utilizes a set to keep track of elements and a list to store the unique elements. It iterates through the unique() list, which has been passed a list of numbers and it will return the unique elements from the list.