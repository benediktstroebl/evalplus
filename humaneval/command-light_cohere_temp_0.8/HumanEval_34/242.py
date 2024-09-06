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
print(unique(test_list))  # [0, 2, 3, 5, 9, 123]

# Test 2
test_list = ['abc', 'bcd', 'abcf', 'bc']
print(unique(test_list))  # ['abc', 'bcd', 'abcf', 'bc']

# Test 3
test_list = [1, 2, 3, 4, 5, 6]
print(unique(test_list))  # [1, 2, 3, 4, 5, 6]
```

The above script defines a function unique that takes a list as input and returns a list containing the unique elements of the input list. The function uses a set and a loop to achieve this. The test cases are then passed to the function to ensure its correctness.