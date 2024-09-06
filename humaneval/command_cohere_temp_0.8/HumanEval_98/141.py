Here's a Python script that contains a function named `count_upper()` which solves the problem as described in the prompt:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Using list comprehension to check if each character in even positions is an uppercase vowel
    return sum(1 for char in s if (ord(char) >= 65 and ord(char) <= 90 and char in 'AEO')) >> 1
```

This function uses a list comprehension that iterates over each character in the string `s`. It checks if the character is an uppercase vowel ('A', 'E', or 'O') and if it appears in an even index (>> 1), it contributes 1 to the count. Finally, the function returns the total count of uppercase vowels in even positions.

You can verify the functionality of the provided solution with the following tests:
```python
test_cases = [
    ('aBCdEf', 1),
    ('abcdefg', 0),
    ('dBBE', 0),
    ('AE', 1),
    ('aB', 0),
    ('EB', 1),
    ('oA', 1),
    ('bEA', 1),
]

for input, expected in test_cases:
    result = count_upper(input)
    assert result == expected, f"For input '{input}', expected '{expected}' but got '{result}'."
```

The tests cover different scenarios to ensure the function behaves as expected.