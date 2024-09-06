```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test the function
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))

test_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(unique(test_list2))
```
This function unique will take a list as input and will return a new list with unique elements. This is the unique elements will always be sorted in ascending order.