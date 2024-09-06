```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0,]] + seen

# Test cases
test_data = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_data)
print("Test Result:", test_result)

test_empty = []
test_result2 = unique(test_empty)
print("Test Result2:", test_result2)

test_duplicates = [3, 3]
test_result3 = unique(test_duplicates)
print("Test Result3:", test_result3)
```
The code defines a function `unique` that takes a list as an argument and returns a new list containing unique elements from the original list. It uses a fact to keep duplicates out and keeps track of elements that have been seen before using a set data structure. The function then is tested using three different test cases: with various lists of different lengths and content. The output displays the unique elements for each test case.