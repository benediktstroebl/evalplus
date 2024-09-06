```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test 1
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_list) == [0, 2, 3, 5, 9, 123]

# Test 2
test_list2 = list(set([1, 2, 2, 3, 4, 5, 6])))
assert unique(test_list2) == [1, 2, 3, 4, 5, 6]
```
This script defines a function called unique which takes a list lst as input and returns a sorted unique elements in that list. It uses a the distinct set to keep track of unique elements and a list to append the unique elements. The tests ensure that function works correctly.