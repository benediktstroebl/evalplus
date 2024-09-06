```python
def pairs_sum_to_zero(lst):
    if sum(map(int, lst)) == 0:
        return "The list has two distinct elements sum to zero."
    else:
        return "The list does not have two distinct elements sum to zero."

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for i, test_tup in enumerate(test_cases):
    print(f"Test {i+1}: {test_tup}")
    result = pairs_sum_to_zero(test_tup)
    print(f"Expected: {'{result}', True)
```
The function pairs_sum_to_zero in this Python code accepts a list of integers as input and returns "True" if the list contains two distinct elements whose sum is zero, and it returns "False" otherwise. The test cases are also a list of test cases that are passed to the function. The expected output is then the correct answer to each test case is displayed.