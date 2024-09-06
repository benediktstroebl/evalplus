```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
 return list(seen))
    return result

# Example usage
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_list)
print(result)  # Output: [0, 2, 3, 5, 9, 123]
```

This function takes a list (`lst`) as input and iterates through it. It uses a unique set to keep track of the elements that have already been seen, and then adds any new elements to the result list. The function then returns a list of unique elements.

The example usage demonstrates how to use the `unique` function with a test list, and prints the resulting unique list.