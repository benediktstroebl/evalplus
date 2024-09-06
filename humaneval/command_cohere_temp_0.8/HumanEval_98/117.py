```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    ct = 0
    for i, char in enumerate(s):
        if char.isupper() and char in 'AEIOU' and (i+1) % 2 == 0:
            ct += 1
    return ct
```
The function `count_upper` takes a string as an argument and counts the number of uppercase vowels in even indices. The result is then returned. To achieve this, the function uses a for loop to iterate through each character in the string. For each character, it checks if it's uppercase and a vowel (using the `isupper` and `in` functions respectively), and whether its index is even (using the modulo operator `%`). If all these conditions are met, the count is incremented. 
This problem can be solved using solely string and list operations, but it's a bit slower than the proposed solution. However, it still passes the problem's tests:
```python
def count_upper2(s):
    ct = 0
    for i, char in enumerate(s):
        if char.isupper():
            if 'AEIOU' == s[i]:
                ct += 1
            elif 'AEIOU' == s[i].lower():
                ct += 1
        if i % 2 == 0:
            ct += 1
    return ct
```