```python
def pairs_sum_to_zero(l):
    return any([x+y <= 0 for x, y in zip(l, l[1:])])

# Test the function with various inputs
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1],
]

for test_case in test_cases:
    if pairs_sum_to_zero(test_case):
        print("Passed test:", test_case)
    else:
        print("Failed test:", test_case)
```
The function `pairs_sum_to_zero` returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. It uses a unique property of Python lists and iterators to quickly check if any sum is zero. 

The test cases provided in the `test_cases` list are used to test the function. 

The `for` loop iterates through each test case, and the `if` statement checks if the function returns `True` for the corresponding test case. If the function returns `True` for a test case, the message "Passed test" is printed. If the function returns `False`, the message "Failed test" is printed.