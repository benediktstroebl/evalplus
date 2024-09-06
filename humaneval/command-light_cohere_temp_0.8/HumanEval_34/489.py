```python
def unique(l: list):
    return sorted(set(l))

# Test the function
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(input_list)
print("Result:", result)

# Test again to ensure stability
input_list2 = [5, 3, 9, 0, 7, 3, 8]
result2 = unique(input_list2)
print("Result2:", result2)
```
This code defines a function `unique` that takes a list `l` as an argument and returns a new list containing the unique elements from `l`. It then creates test cases with input lists, calls the `unique` function with those lists, and prints the results. Finally, the function is tested again with different input lists to ensure the uniqueness of the results.

This code is self-contained and provides the desired functionality without requiring external dependencies.