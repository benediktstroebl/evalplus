```python
def unique(l: list):
    return list(set(l))

# Test the function with a sample input
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_unique)
print("Result:", result)

# Test the function again with list of strings
string_list = ["Hello", "World", "!!", "!!!"]
result_strings = unique(string_list)
print("String result:", result_strings)
```