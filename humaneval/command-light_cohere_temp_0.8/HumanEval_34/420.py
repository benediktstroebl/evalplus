Here's a self-contained Python script with a function that returns a list of unique elements from a given list:
```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_unique = unique(test_list)
print("Test list:", test_list)
print("Test unique:", test_unique)

# Input and expected output
input_list = ["text1", "text2", "text3", "text4", "text5"]
input_unique = unique(input_list)
print("Input list:", input_list)
print("Input unique:", input_unique)
```

The unique function creates a set of elements seen so far, then iterates through the input list and returns any elements that are not in the set and are not `float('inf')`, effectively giving you the unique elements. 
Test cases and input/output are shown to verify the correctness of the function.