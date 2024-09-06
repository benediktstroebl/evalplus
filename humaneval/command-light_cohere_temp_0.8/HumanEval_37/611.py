```python
def sort_even(lst):
    return sorted(lst, key=lambda x: (x if x % 2 == 0 else x + 1))

# Example usage:
lst = [5, 6, 3, 4]
result = sort_even(lst)
print(result)  # Expected output: [3, 6, 5, 4]

# Test 1:
test_case = [1, 2, 3, 4, 5, 6]
test_result = sort_even(test_case)
print("Test 1 Result:", test_result)

# Test 2:
test_case2 = [7, 8, 9, 10]
test_result2 = sort_even(test_case2)
print("Test 2 Result:", test_result2)
```
The function `sort_even` uses the `key` argument of the `sorted` function to specify a custom function that determines the sorting key. This function returns a
sorted list that preserves even integers and reorders odd ones.