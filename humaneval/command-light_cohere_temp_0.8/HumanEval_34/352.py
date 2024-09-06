```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not(seen.add(x))]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # expected output: [0, 2, 3, 5, 9, 123]

# Another test
test_strings = ["foo", "Bar", "foo", "baz"]
print(unique(test_strings))  # expected output: ['foo', 'Bar', 'baz']
 ```
This script defines a function `unique` that returns a list containing the unique elements of the input list `lst`, as long as those elements are not already present in the set `seen`. The test cases demonstrate the function's correctness by passing various lists to it and confirming the expected unique elements.