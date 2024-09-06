```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    LC = s.lower()
    return sum(1 for i, char in enumerate(LC) if i % 2 == 0 and char in 'AEIOU' and char == s[i].upper())
```

This code utilizes a generator expression alongside the `sum()` function to determine the count of uppercase vowels in even indices of the string. It examines each character in the string, checking if it's an uppercase vowel ('AEIOU') and if it appears in an even index. The sum of these evaluations determines the total count. The lowercase counterpart is also generated to aid in the process.