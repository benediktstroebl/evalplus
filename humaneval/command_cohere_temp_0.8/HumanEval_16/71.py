Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store unique characters in the provided string, regardless of case. It first converts the input string to lowercase using the `lower()` method, thus ensuring that characters in the string are treated as the same regardless of case. The converted string is then used to update the set, automatically removing duplicate characters. The function finally returns the count of distinct characters in the set. 

The tests for this function can be executed using the following code:
```python
test_cases = [
    ("xyzXYZ", 3),
    ("Jerry", 4),
    (# Added a new test case to cover multiples of the same character)
    ("iiiiii", 1),
    # Add more test cases as needed
]
for input, expected in test_cases:
    assert count_distinct_characters(input) == expected
```
This block of code provides a series of test cases with corresponding expected values. The `count_distinct_characters` function is then applied to each input, and the results are compared using assertions to ensure that the function's outputs align with the expected values.