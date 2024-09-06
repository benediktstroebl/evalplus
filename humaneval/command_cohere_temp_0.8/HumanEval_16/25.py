Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to handle the distinct characters regardless of case and returns the count of these distinct characters.

To test this function, you can run the following code:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    (# Tests with none-alphabetic characters
    ('123abc', 3),
    ('P3@#%^-', 4),
    # Tests with single character string
    ('a', 1),
    ('A', 1)
])

for test_case in test_cases:
    assert count_distinct_characters(*test_case) == test_case[1]
```
This block of code provides test cases to ensure that the function `count_distinct_characters` works correctly. Each test case is a tuple containing the input string and the expected output. The `assert` statement checks that the output of the function is correct for each test case.  This combined with the script above provides a complete self-contained solution to the problem.