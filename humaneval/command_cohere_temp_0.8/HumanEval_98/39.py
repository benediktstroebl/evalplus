```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    modified_s = ['A','a','E','e','I','i','O','o','U','u','Y','y'].index(c) for c in s if c.isupper() and c in 'AEIOU'
    return sum(modified_s)
```
The problem is quite interesting and requires understanding a couple of concepts:
1. To solve this problem, it is crucial to identify the vowels and the even indices. Python provides a built-in function `isupper()` that checks if a character is uppercase, and `index` assists in finding the position of the character in the string. This helps to recognize the required characters in even indices.
2. To solve this problem, it would be beneficial to use Python's `enumerate` or `zip` functions. These enable us to pair each character in the string with its index, allowing us to check if the character is an uppercase vowel and if it sits in an even index.

This solution utilizes a combination of these concepts, along with Python's innate capabilities, to deliver a concise and effective approach.