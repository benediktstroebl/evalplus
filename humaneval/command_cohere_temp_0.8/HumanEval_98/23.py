Here's a Python script that contains a function named `count_upper()` which solves the problem as described in the prompt:
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

This function takes a string `s` as its argument and first creates a list called `vowels` that contains all the uppercase vowels (`AEIOU`). It then initializes a counter variable `count` to 0.

The function then loops through the characters of the input string `s` in increments of 2 using a `for` loop. It checks if the character is uppercase and if it's a vowel, adding 1 to the counter variable `count` for each such character.

Finally, the function returns the total count of uppercase vowels in even indices of the string.

This code should accurately solve the problem and produce the correct output for the given test cases. You can use it as a self-contained Python script to tackle the problem.  Any string you pass to the function will return the number of uppercase vowels in even indices as requested.  For instance:
```python
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))  # Output: 0
``` 
You can add more test cases to ensure its robustness and verify that the function is correctly counting the uppercase vowels in even indices as intended.