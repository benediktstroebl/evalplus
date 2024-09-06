```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Iterate through each character in the string
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which takes a string `s` as an argument and returns the number of uppercase vowels in even indices of that string. The function counts the number of vowels and increments the counter if the character is in an even index and is an uppercase vowel. The script passes the given tests: `count_upper('aBCdEf')` returns 1, `count_upper('abcdefg')` returns 0, and `count_upper('dBBE') returns 0.` 

These test cases ensure that the behavior matches the problem statement for a wide range of inputs.  If you would like to test this script with different strings, you can modify the test cases as needed.