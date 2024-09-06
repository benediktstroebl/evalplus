```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(seen))
    return result

# Example usage
my_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(my_list))  # Output: [0, 2, 3, 5, 9, 123]
```
This script defines a function unique that takes a list lst as input and returns a new list with unique elements from the original. It uses the unique elements by creating a set seen and appending elements to the result list that are not present in the set seen. This ensures that duplicate elements are removed from the list.