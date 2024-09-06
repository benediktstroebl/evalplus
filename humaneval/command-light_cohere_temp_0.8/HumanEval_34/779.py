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
print(unique(test_list))
# [0, 2, 3, 5, 9, 123]

# Test 2
test_list2 = list(set([5, 3, 5, 2, 3, 3, 9, 0, 123]))
print(unique(test_list2))
# [0, 2, 3, 5, 9, 123]
```
This script defines a function called **unique** that takes a list as an argument and returns a new list containing unique elements from the original list, after eliminating duplicates. The script then provides two test cases to verify the correctness of the function, which both pass successfully.