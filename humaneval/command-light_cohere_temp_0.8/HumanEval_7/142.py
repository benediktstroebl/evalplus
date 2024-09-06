Here's the function and the tests:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]

# Test cases
test_cases = [
    [],    # Empty input
    ['abc', 'bacd', 'cde', 'array'],  # Input contains the substring
    ['words', 'abc123', 'abcd'],     # Input does not contain the substring
]

test_by_substring(test_cases, 'a')
```
This function takes two parameters - a list of strings (strings) and a substring (substring). It returns a new list containing only the strings from the input list that contain the substring at any position.