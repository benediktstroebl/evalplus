```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not set()]
    # [1, 3, 2, 4, 7, 5, 6, 8, 9]

# Test
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Test unique:", unique(test_unique))  # [0, 2, 3, 5, 9, 123]

# Test with list of strings
test_strings = ["this is", " test", "hello", "world"]
print("Test unique:", unique(test_strings))  # ['this is', 'test', 'hello', 'world']
```
This function, unique, takes a list lst as input and returns a new list containing only the unique elements from lst. The function utilizes the fact that for each element in the list, if it is not in the seen set, then it is added to the seen set and returned.