Here's a Python script that contains a function `count_upper()` which solves the problem as described in the prompt:
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

This function takes a string `s` as its argument and first creates a boolean list `vowels` with the uppercase vowels 'AEIOU'. It then iterates through the characters of the string, checking if each character is upper case and is a vowel, and if the index of the character is even. If both are true, it increments the counter. Finally, it returns the total count.

You can test this function using the following code:
```python
test_cases = [('aBCdEf', 1), ('abcdefg', 0), ('dBBE', 0)]
for case in test_cases:
    assert count_upper(*case) == case[1]
```

This block of code contains a list of test cases, where each test case is a tuple containing the input string and the expected output. The `assert` statement checks if the output of the `count_upper()` function is equal to the expected output for each test case and throws an error if they are not equal. 

To execute this code block, you can utilize a Python compiler and runner, which will run the tests and display any errors or results.