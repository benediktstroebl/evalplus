```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    return [lst[0] + 1, lst[1] + 1, lst[2] + 1]

# Test cases
test_incr_list = [
    [(1, 2, 3)],
    [(5, 3, 5, 2, 3, 3, 9, 0, 123)],
    [],
    [(1, 2, 7),(3, 9, 12)],
    [(-1, -10, -100), (-5, -3, -25)],
]

# Loop through test cases
for l in test_incr_list:
    # Call function with test case
    result = incr_list(l)

    # Check if result matches expected output
    if result != l:
        print("Incorrect result for input", end="")
        print(f"Expected: {l[0]} + {l[1] + {l[2]}", end="")
        print("Got:", end="")
        print(result)
        print("="*5)
        break
```

This script defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The test cases are defined as a list of tuples, each containing the input list and the expected output. The script then loops through each test case, calls the `incr_list` function with the input, and checks if the result matches the expected output.

The output will display the error message for incorrect inputs.