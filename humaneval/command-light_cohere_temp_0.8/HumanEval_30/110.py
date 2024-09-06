```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite with defined function
test_get_positive = []
test_cases = [
    [([-1, 2, -4, 5, 6], [2, 5, 6])],
    [(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10), [5, 3, 2, 3, 9, 123, 1]])
]

def test():
    res = get_positive(test_cases[0][0])
    print("First test:", res)
    res = get_positive(test_cases[1][0])
    print("Second test:", res)

# Run the test suite
test()

```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. 

The test suite consists of two test cases, each containing a list of values and the expected output of the `get_positive` function. 

The test suite is executed using the `test()` function, which runs the `get_positive` function on the provided test cases and prints the results.