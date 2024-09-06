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
The problem is relatively straightforward. You iterate through the string s, considering every even index, and for each index, you check if the character is an uppercase vowel. You return the count. To optimize, you don't check if the character is an uppercase vowel each time; instead, you do it once when the function starts, and you use an inline dictionary to map the characters to 1, thereby cutting down the number of operations substantially.