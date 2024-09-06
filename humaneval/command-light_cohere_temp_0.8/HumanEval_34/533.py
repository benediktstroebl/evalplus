```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in set()]
    seen.add(lst[0])
    return seen

# Test case 1:
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))

# Test case 2:
test_case2 = [1, 2, 4, 3, 5, 6, 7]
print(unique(test_case2))
``` 
This code defines a function `unique` that returns a set of unique elements from the input list. It uses a unique values in the list, sets to quickly identify duplicates. The code is well-contained and can be easily imported and used in other Python scripts.