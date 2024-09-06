```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
        return result
    ```

# Test 1
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_list)
print(result)

# Test 2
test_list2 = [4, 6, 2, 98, 97, 99]
result = unique(test_list2)
print(result)

# Test 3
test_list3 = [100, 101, 102]
result = unique(test_list3)
print(result)
```