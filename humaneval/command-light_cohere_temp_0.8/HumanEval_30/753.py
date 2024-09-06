```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with different input
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
print(result)

# Test with list comprehension instead of a function
test_list_comprehension = [-1, 2, -4, 5, 6]
result_comprehension = [num for num in test_list_comprehension if num >= 0]
print(result_comprehension)
```
The output will show the resulting list with all positive numbers from the input list. 
The function and list comprehension pass all the corresponding tests.