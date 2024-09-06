```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x.x)
    unique() list: [0, 2, 3, 5, 9, 123]
    print(result)  # Output: [0, 2, 3, 5, 9, 123]
``` 
This function takes a list as input and creates a set to keep track of the unique elements. It then iterates through list and adds each element to the set, which automatically adds it to the unique set of unique elements. 

After processing the entire list, it builds a new list, `result`, containing all the unique elements from the original list. 

This script is self-contained and does not require any external modules or functions.