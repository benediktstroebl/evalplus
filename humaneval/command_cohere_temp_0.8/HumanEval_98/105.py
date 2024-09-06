Here's the Python code with a function that solves the problem:
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

This function `count_upper()` takes a string s as input and counts the number of uppercase vowels in even indices. It utilizes a for loop to iterate through the characters of the string at even indices, checks if the character is an uppercase vowel, and increments the count if it meets both conditions. The function returns the final count of uppercase vowels in even indices. 

The markdown code block for this solution is:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
```