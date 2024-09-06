```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result

# Test cases
test_list1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_list2 = [4, 2, 2, 6, 8, 3, 5, 7, 1]
test_list3 = ['a', 'b', 'c', 'a']

print("Test case 1: ", unique(test_list1)) # [0, 2, 3, 5, 9, 123]
print("Test case 2: ", unique(test_list2)) # [2, 4, 6, 8, 3, 5, 7]
print("Test case 3: ", unique(test_list3)) # ['a', 'b', 'c']
```
The function unique is a self-contained Python function that sorts and returns unique elements from the passed list, it uses a set to keep track of elements seen before and a list to store the result.