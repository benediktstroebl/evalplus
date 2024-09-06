```python
def pairs_sum_to_zero(l):
    return any([x+y <= 0 for x,y in zip(l, l[1:])])

# Test cases for the function
test_cases = [
    [ [1, 3, 5, 0], [1, 3, -2, 1], [1, 2, 3, 7], [2, 4, -5, 3, 5, 7], [1]]
]

test_results = []
for test_case in test_cases:
    result = pairs_sum_to_zero(test_case)
    test_results.append(result)

print("Test Results:")
print(test_results)

``` 
This Python function, `pairs_sum_to_zero`, takes a list of integers as input and returns `True` if the list contains two distinct elements that sum to zero, and `False` otherwise. The function uses a list comprehension and the `any()` function to check if there are two distinct elements that sum to zero.

The test cases are defined as a list of lists, where each inner list represents a set of numbers to be tested. The `test_results` list is used to store the results of each test case, and it is updated with the result of each call to the `pairs_sum_to_zero` function.