```python
def pairs_sum_to_zero(lst):
    if not sum(lst) == 0:
        return "Yes"
    else:
        return "No"

# Test cases for function
test_pairs_sum_to_zero = []
test_pairs_sum_to_zero.append([1,3, -2,1])
test_pairs_sum_to_zero.append([2,4, -5,3,7])
test_pairs_sum_to_zero.append([1])

for test_case in test_pairs_sum_to_zero:
    print(f"{test_case[0]} { test_case[1]}  sums to {test_case[2]}")
    result = pairs_sum_to_zero(test_case)
    print(f"Result: {result}")
```
This code defines a Python function `pairs_sum_to_zero` that takes a list of integers as an argument. It checks whether the by the sum of the elements in the list equals zero, the function returns "Yes". The code then provides several test cases to verify the function, each consisting of two elements, and a boolean indicating whether their sum is zero or not. The test cases are stored in the list `test_pairs_sum_to_zero`, and the function is called with each test case. The output is then printed, which displays the result of the function for each test case.