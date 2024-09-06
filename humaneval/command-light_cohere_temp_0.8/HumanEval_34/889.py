```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # [0, 2, 3, 5, 9, 123]

test_string = "  # This is a string with special characters   # " and #
test_string = ['a', 'aa', 'ccc', '#']
print(unique(test_string))  # []

test_set = set([1, 2, 3, 4, 5])
print(unique(test_set))  # [1, 2, 3, 4]

test_custom = [4, 5, [1, 2, 3], 6]
print(unique(test_custom))  # [4, 5, [1, 2, 3], 6]
```
The `unique` function in this code accepts a list (`lst`) as an argument and uses a set (`seen`) to maintain the distinct elements. The function then iterates through each element in the input list and adds the element to the set if it hasn't been seen before. Finally, the function returns a list containing only the distinct elements.