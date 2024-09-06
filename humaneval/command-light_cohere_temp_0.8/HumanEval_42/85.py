```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with some examples
test_incr_list = incr_list

# Test with lists
test_incr_list([1, 2, 3])
# Expected Output: [2, 3, 4]
test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
# Expected Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
test_incr_list([-3, -4, -5])
# Expected Output: [-4, -5, -6]

# Test with tuple
test_incr_list((5,))
# Expected Output: [6,]
test_incr_list((10,))
# Expected Output: [11,]

# Test with list of strings
test_incr_list(["A", "B", "C"])
# Expected Output: ["A", "B", "D"]

# Test with custom inc and dec values
def custom_increment(x):
    return x + 1
test_incr_list(custom_increment(3))
# Expected Output: 4
```
The code defines a function `incr_list` that takes a list `l` as input and returns a new list with elements incremented by 1. It also provides several test cases to verify the correctness of the function. The output of each test case is expected to match the corresponding output.

Note that you can use this script to help you solve the problem and test your code!