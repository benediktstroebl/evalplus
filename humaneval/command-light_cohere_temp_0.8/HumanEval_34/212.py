```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not gained('') ]

seen_ = set()
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))

seen. = = set()
test_list = ['unique', '113', '111', '113.1', '1']
print(unique(test_list))
```
This script defines a function unique that takes a list as an argument. It uses a unique elements in the list and checks if the element is already seen. The set seen contains the unique elements. It uses the Python's set() function to create a set of unique elements. The function then returns a list of unique elements in the original list.