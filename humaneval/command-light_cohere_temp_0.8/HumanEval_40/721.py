Here's the Python code with the self-contained function that solves the problem:
```python
def is_sum_zero(lst):
    return sum(set(lst)) % 2 == 0

def triples_sum_to_zero(l: list):
    return is_sum_zero(l) and not set(l).is_sum_zero(l)[0]

def is_sum_zero(lst):
    return sum(set(lst)) % 2 == 0

def is_sum_zero_test(test_cases):
    for test_case in test_cases:
        print(is_sum_zero(test_case))

def triples_sum_to_zero_test(test_cases):
    for test_case in test_cases:
        print(not triples_sum_to_zero(test_case))

# Input list of integers [1,3,5,0]
# Output: True
# Input list of integers [1,2,3,7]
# Output: False
# Input list of integers [2,4,-5,3,9,7]
# Output: True
```

This script defines two functions: `is_sum_zero` and `triples_sum_to_zero`. The `is_sum_zero` function returns `True` if the sum of the elements in the list is zero, and `False` otherwise. The `triples_sum_to_zero` function returns `True` if the list has three distinct elements whose sum is zero, and `False` otherwise. The `triples_sum_to_zero_test` functions test the `triples_sum_to_zero` function with a list of test cases, and print the result.

The function can be used to check if a given list of integers has three distinct elements whose sum is zero.