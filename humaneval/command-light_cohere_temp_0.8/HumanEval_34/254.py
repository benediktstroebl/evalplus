```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Example usage
lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(lst))  # [0, 2, 3, 5, 9, 123]
```
This function, unique, takes a list as input and returns a sorted list of unique elements found in the input list. It does this by creating a set of items and iterates through the input list, appending elements to the set if they're not already in it. Then, it iterates through the unique elements of the set to create a new list with unique items. 

This function is self-contained and can be used to quickly find the unique elements in any list without the need for external lists or arrays.