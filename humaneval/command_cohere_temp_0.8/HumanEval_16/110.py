Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same character. The function then returns the length of this set, which is the number of distinct characters in the string.

To test this function, you can run the following code:
```python
test_cases = [
    ("xyzXYZ", 3),
    ("Jerry", 4),
    (# Tests with empty string and non-string inputs should also be added for completeness, 
]

for test_case in test_cases:
    assert count_distinct_characters(*test_case) == test_case[1]
```
This block of code provides test cases that cover different scenarios and verifies that the function `count_distinct_characters` returns the expected output for each case. 

Make sure to add appropriate protections and testing strategies appropriate to your needs.  Please let me know if there's anything else I can contribute to the solution or provide further feedback on testing strategies.