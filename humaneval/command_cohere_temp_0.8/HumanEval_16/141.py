Here's a Python script that contains a function called `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The function `count_distinct_characters` works by first creating a set of all the characters in the given string, where duplicates are automatically removed, and then returns the count of that set. The conversion to lowercase ensures that characters in the string are treated case insensitively. 

To ensure the robustness of the function, it's a good idea to add tests based on the prompts provided:
```python
# Tests:
test_cases = [
    ("xyzXYZ", 3),
    ("Jerry", 4),
    # Add more test cases here to cover corner cases if necessary
]
for given_string, expected in test_cases:
    assert count_distinct_characters(given_string) == expected
```