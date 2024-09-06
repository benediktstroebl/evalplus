Here is a self-contained Python script that solves the problem of finding all prefixes from shortest to longest of an input string:
```python
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ''] + [''] * (len(string) - 2)

# Test cases
test_cases = [
    'abc',
    'foo',
    '',
    '123',
    'abc123',
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    print(f'Test case: {test_case} => {', ', '.join(actual_prefixes)})
    print()
```

The above code defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of the input string. This is done iteratively by using a list comprehension that creates prefixes from characters in the string, and a "null" character to exclude from the current prefix.  The also use the and add a "null" character at the end for every prefix less than or equal to the current length of the string.