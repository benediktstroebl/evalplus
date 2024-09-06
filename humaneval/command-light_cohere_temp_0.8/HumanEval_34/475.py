Here is a self-contained Python script that solves the problem of finding unique elements in a list:
```python
def unique(lst):
    return list(set(lst))

# Test the function with a sample list
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
# Call the unique function and print the result
unique_result = unique(test_list)
print("Unique elements:", unique_result)

# Test the function with a list of strings
string_list = ["item1", "item2", "item3", "item4"]
# Call the unique function and print the result
unique_result_string = unique(string_list)
print("Unique elements:", unique_result_string)
```

Please note can find this code helpful as it provides a complete solution to the given problem with full self-containance.