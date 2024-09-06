Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. The function outputs are consistent with the given test cases.

```python
tests = [
    ([1, 2, 3], [2, 3, 4]),
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124]),
]

for idx, test in enumerate(tests, start=1):
    assert incr_list(test[0]) == test[1], f'Test {idx} failed'
```
This script also includes a battery of tests contained in the `tests` variable, which comprises list inputs and their corresponding expected output. The function provides an `assert` statement that verifies if the output of `incr_list` corresponds with the expected output for each test case. If the assertion is successful, it signs the test case off; otherwise, it returns an error message that mentions the failed test. 

The function is designed to be standalone and can be run directly to test it. Additionally, you can execute the `tests` dictionary to validate the function across different inputs.  This approach provides a straightforward way to ensure the function remains correct over time and survives any potential code changes.