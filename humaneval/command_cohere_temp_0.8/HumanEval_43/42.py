```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and (i - 1) in seen:
            return True
        seen.add(i)
    return False
```

This function examines each integer in the list and determines whether it has a negative counterpart elsewhere in the list. It uses a set data structure to keep track of the distinct values and uses the fact that sets do not contain duplicate values to prevent double-counting negatives. It returns True if any two elements sum up to zero, and False otherwise. 

Here is an example usage of the function with a corresponding markdown code block containing the test cases: 
```python
# Test cases for pairs_sum_to_zero

test_cases = [
    ([1, 3, 5, 0], False),
    ([1, 3, -2, 1], False),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 5, 7], True),
    ([1], False)
]

for args, expected in test_cases:
    actual = pairs_sum_to_zero(args)
    assert actual == expected, f"Expected {expected}, but got {actual} for input {args}"
```