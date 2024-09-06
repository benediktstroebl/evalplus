Here's a Python script with a function that solves the problem as described in the code block:
```python
def count_upper(s):
    upper_vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function `count_upper` takes a string `s` as input and counts the number of uppercase vowels in even indices. It utilizes a dictionary `upper_vowels` to store the uppercase vowels, checks each character in even indices to see if it's uppercase and a vowel, and increments the count if it is. The function finally returns the total count of uppercase vowels in even indices. 

You can use this function with the given test cases to verify its behavior:
```python
test_cases = [
    ('aBCdEf', 1),
    ('abcdefg', 0),
    ('dBBE', 0),
    ('AEEIOU', 5),
    ('ABCCDDZZZZ', 3),
]

for case in test_cases:
    input_str, expected = case
    actual = count_upper(input_str)
    assert actual == expected, f'For input:{input_str}, expected {expected}, got {actual}'
```

This code snippet encapsulates the problem in a test-driven manner, ensuring the function behaves as expected for various inputs.