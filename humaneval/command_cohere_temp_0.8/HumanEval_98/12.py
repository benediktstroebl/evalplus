```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which:
1. Defines a set named `upper_vowels` containing all uppercase vowels: 'A', 'E', 'I', 'O', and 'U'.
2. Initializes a variable `count` to zero, aiming to count the number of uppercase vowels in even indices.
3. Utilizes a loop that iterates through the string `s` with a step size of 2 (to only consider even indices).
4. For each iteration, it checks if the character is uppercase and belongs to the set of uppercase vowels.
5. If the condition is met, it increments the count.

The script efficiently solves the problem in a straightforward manner. It can be tested with the following input to match the given test cases:
```python
test_cases = [
    ('aBCdEf', 1),
    ('abcdefg', 0),
    ('dBBE', 0),
]

for input_string, expected in test_cases:
    output = count_upper(input_string)
    assert output == expected, f"For input:{input_string}, Expected:{expected} Actual:{output}"
```

This test suite covers all the edge cases provided in the problem statement and verifies the correctness of the `count_upper()` function.