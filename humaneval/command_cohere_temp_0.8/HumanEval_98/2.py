```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = {"A":1, "E":1, "I":1, "O":1, "U":1}
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels and s[i].isupper():
            count += 1
    return count
```
The problem is relatively straightforward. You iterate through the string `s` incrementing `count` whenever an uppercase vowel is encountered at an even index. The `upper_vowels` dictionary provides a convenient way to filter out lowercase vowels. 
For edge cases, the loop is flanked with `range(0, len(s), 2)` to only iterate through even indices, and the `if` condition filters for uppercase vowels. 
The provided tests in the problem statement would be useful in ensuring that the function is correctly implemented. It's always a good practice to test with a variety of inputs, including edge cases and different variations of vowels and alphabets. 
I hope this helps, let me know if you need anything else!