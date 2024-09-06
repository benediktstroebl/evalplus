```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as input and returns a sorted list of all elements that do not have any even digits. The `not any()` function is used to efficiently check if any element of the string representation of the integer has a digit that is even. The returned list is sorted in increasing order, as specified in the note in the problem statement.

Here is a simple test case to verify the functionality of the function:
```python
test_cases = [[15, 33, 1422, 1], [152, 323, 1422, 10]]

for case in test_cases:
    assert unique_digits(case) == [1, 15, 33], "Failed case: {} {}".format(case, unique_digits(case))
```

This test case uses an `assert` statement to check if the output of the `unique_digits` function is equal to the expected output for each element of the test case.