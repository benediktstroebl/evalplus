Here is a Python script with a self-contained function that solves the problem of finding three distinct elements in a list that sum to zero:
```python
def is_sum_to_zero(lst):
    return all(map(sum, lst)) and sum(map(sum, lst)) < 0

def triples_sum_to_zero(l: list):
    return is_sum_to_zero(l) and len(l) > 2

# Test cases
tests = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 9, 7],
    [1],
    ]

for i, test in enumerate(tests):
    result = triples_sum_to_zero(test)
    print(f"{i+1}: {result}")
```

This script defines two functions:
- The `is_sum_to_zero` function checks if all elements in a list sum to zero.
- The `triples_sum_to_zero` function takes a list of integers and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.

The script then provides test cases to verify the correctness of the function. 

The output will display the result of each test case, showing whether the function returns `True` or `False`.