```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x.append(x unique))
   
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result_test = unique(test_list)
print("Test 1 Result:", result_test)

test_list2 = [3, 'abc', 12345]
result_test2 = unique(test_list2)
print("Test 2 Result:", result_test2)
```
The function unique takes a list as input and returns a new list containing unique elements from the original list. It uses the optimized approach to achieve this, and the function and test cases are self-contained, meaning they can be copied and pasted as-is without the need for additional code or modules.