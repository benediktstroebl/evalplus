Here is a self-contained Python function that solves the problem of sorting and returning unique elements from a list: 

```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x, x)
    return result
``` 

This function uses a set to track unique elements and a list to store the unique elements. The function iterates through each element in the list and checks if it's already in the set. If it's not, it adds the element to both the set and the list of unique elements. 

This function can easily be used in any program or script without the need for external variables or external code.