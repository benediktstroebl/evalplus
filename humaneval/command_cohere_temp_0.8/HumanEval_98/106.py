Here's a Python script that contains a function named `count_upper()` which solves the problem as outlined in the markdown code block you provided:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This function takes a string s as input and counts the number of uppercase vowels present in even indices of the string. It utilizes the isupper() method to determine if a character is uppercase and checks if it's a vowel using a predefined vowels string. The function then returns the count of such characters in even indices.

To test this function, you can use the following code:
```python
test_cases = [
    ('aBCdEf', 1),
    ('abcdefg', 0),
    ('dBBE', 0),
    ('ABCEFG', 2),
    ('BCDEfa', 1),
]

for case in test_cases:
    assert count_upper(case[0]) == case[1]
```

This block of code uses a list of test cases, where each element of the list is a tuple containing the input string and the expected output. It then checks if the output of the `count_upper()` function for each input string is correct, using the `assert` statement to check if the output matches the expected result.