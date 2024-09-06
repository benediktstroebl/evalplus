Here is a Python script with a self-contained function that solves the problem you have described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    """
   
    frequency = 0
    for char in substring:
        if char in string:
            frequency += 1
    return frequency

# Test cases
test_cases = [
    ("", "a"),
    ("aaa", "a"),
    ("aaaa", "aa"),
    (uuuuuuuu", "a"),
    ( "", "" )
]

for test_case in test_cases:
    print(f"The frequency of {test_case[1]} in {test_case[0]} is: {how_many_times(test_case[0], test_case[1])}")
```
This code defines a function that counts the frequency of a given substring in a given string. It then tests these function with different test cases to verify its functionality.