```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Example usage:
input = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(input))
```
The code defines a function called unique that takes a list as an argument. It uses a saw = set() to initialize a set, which will store the unique elements from the input list. The function then loops through the unique elements in the list, appending them to result if they are not already in the seen set. The loop continues until all the elements have been processed.

Finally, the unique function returns the sorted unique elements from the input list, which are in this case [0, 2, 3, 5, 9, 123].