```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, []]]

# Test cases
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, [123]]
test_list = [5, 3, 7, 8, 9, 2, 4, 6]
test_empty = []

# Test results
print(unique(test_unique))  # Expected output: [0, 2, 3, 5, 9, 123]
print(unique(test_list))   # Expected output: [5, 8, 9, 2, 4, 6]
print(unique(test_empty))  # Expected output: []
```

The code defines a function unique that takes a list as an argument and returns a new list with unique elements from the original list. It utilizes a unique elements within the the set to keep track of elements already encountered and only returns elements that are not in the set, not in the original list, and not [-None, []]. The test cases include lists with different sizes and empty lists, and the output is expected to be as specified. 

Note: The output may vary when you run the code due to how Python's set behaves.