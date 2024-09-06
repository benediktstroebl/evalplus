```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x do.append(x unique))
    return result

# Test cases
test_data = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_data)
print("Test case 1:", test_result)

test_data2 = [1, 2, 3, 4, 5, 6]
test_result2 = unique(test_data2)
print("Test case 2:", test_result2)

test_data3 = [8, 7, 9, 1, 5, 3]
test_result3 = unique(test_data3)
print("Test case 3:", test_result3)
```
The function unique in the provided script accepts a list lst and returns a list of unique elements in that list. The function employs the distinct set seen to monitor the already seen elements and a new empty list result to record the new elements that haven't been seen before. The code is self-contained and can be used to quickly solve the issue of obtaining a list of unique elements in a given list.