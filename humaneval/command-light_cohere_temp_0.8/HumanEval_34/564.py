```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # expected output: [0, 2, 3, 5, 9, 123]

test_string = "## Unique elements ##" + "\n" + "   " + [5, 3, 5, 2, 3, 3, 9, 0, 123] + "\n" + "  "
print(unique(test_string.split('\n"))  # expected output: [0, 2, 3, 5, 9, '## Unique elements ##']

test_set = {5, 3, 5, 2, 3, 3, 9, 0, 123}
print(unique(test_set))  # expected output: [0, 2, 3, 5, 9, 123]
```
The function `unique` takes a list `lst` as input and initializes an empty set `seen` to keep track of the elements we have encountered so far. It then iterates through elements in the list and, for each element, it checks if it's already in the seen set. If the element is not seen, it's added to the set and then added to the result list. The `result` list is returned and it contains all the unique elements from the original list.