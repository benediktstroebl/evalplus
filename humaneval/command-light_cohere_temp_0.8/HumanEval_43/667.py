```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test cases are provided to ensure the function is working correctly. 
"""
    for x in range(10):
        y = x + 1
        if l[x] + l[y] == 0:
            return True
        else:
            return False
    """

# Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1],
]

# Function call
for x in test_cases:
    if pairs_sum_to_zero(x):
        print(f"{x} passed the test.")
    else:
        print(f"{x} failed the test.")
```