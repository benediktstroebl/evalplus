```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   list)
    return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # expected output: [0, 2, 3, 5, 9, 123]

test_string = "## Unique elements ##"
for x in unique(["hello", "world!"]):
    print(x, end=" ")
print() 
```  This script defines a function `unique` that takes a list as input and returns a list of unique elements from that list, which are stored in a set. The function uses a set to keep track the unique elements. 

The test cases are also included in this script, and the output of the function is printed to ensure it is working correctly.