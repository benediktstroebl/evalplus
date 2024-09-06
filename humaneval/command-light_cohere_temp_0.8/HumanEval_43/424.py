```python
def pairs_sum_to_zero(l):
    return any(x + y == 0 for x, y in zip(l, l[1:]))

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

test_run = testcase_suite('pairs_sum_to_zero', test_cases)

# Print the result
print("The sum of the elements in the list is:", end="")
for test in test_run:
    print(test[1], end=" ")
```
The function 'pairs_sum_to_zero' in the code above determines whether the sum of two elements in the list is equal to zero. The first element in the list is used to iterate through the second list and determine whether their sum is zero. 

The test cases are defined in the test_cases list, which contains lists that will be used to test the 'pairs_sum_to_zero' function. The function will be tested against each test case and the result will be stored in the test_run list. Finally, the test results will be printed to the console.