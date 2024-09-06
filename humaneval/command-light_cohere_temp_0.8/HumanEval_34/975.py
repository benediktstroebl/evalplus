```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
        unique(seen)
    return result

# Test case
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_list)
print(result)  # Expected output: [0, 2, 3, 5, 9, 123]
```
This script defines a function unique that takes a list lst as input and returns a new list with unique elements from the original list. The function uses a set to keep track of elements seen so far and then appends the remaining unique elements into a new list result. 

Finally, the test case is provided to demonstrate the usage of the function. The output of the function is then expected to be the desired unique elements of the test list.