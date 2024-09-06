```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not (-1)]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))

# Test case 2
test_case2 = [5, 3, (5), 0]
print(unique(test_case2))

# Test case 3
test_case3 = ['a', 'a', 'b']
print(unique(test_case3))
```
The function unique takes a list as input and uses a set to store unique elements from the list. It iterates over each list and adds elements to the set if they are not duplicates. The function then returns a list containing the elements from the input list that are not in the set.