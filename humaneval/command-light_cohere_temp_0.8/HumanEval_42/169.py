```python
def incr_list(lst):
    lst.add = [list.__additem__
	for item in lst:
		add(item + 1)
	return lst

# Test 1
test1 = [1, 2, 3]
# Test 2
test2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]

print(incr_list(test1))
print(test1)
print(incr_list(test2))
print(test2)
```
This code defines a function `incr_list` that increments each item in the input list by 1. It uses the list's built-in function `add` to add an item to the list. It then returns the string-formatted test results.