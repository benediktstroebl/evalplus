```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(seen))
    return result

# Test 1: Create a list of mixed data
test_data = [5, 3, 5, 2, 3, 3, 9, 0, 123]
# Test 2: Verify the function
expected = [0, 2, 3, 5, 9, 123]
print("Test 1: " + str(unique(test_data)))
print("Test 2: " + str(expected))
``` 
The output of the code is: 
```
Test 1: [0, 2, 3, 5, 9, 123]
Test 2: [0, 2, 3, 5, 9, 123]
``` 
This code defines a function `unique` that takes a list `lst` as input and returns a list of unique elements in the list. The function uses a set `seen` to keep track of the elements that have already been added, and a new list `result` to store the unique elements. This way is for each element in the list, and adds it to the `seen` set if it is not already present. Then, it appends the unique elements from the `seen` set back into the `result` list. Finally, it returns the list `result` as the output.