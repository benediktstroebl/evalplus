Here's a Python script that contains a function which takes a string as an input and returns the number of uppercase vowels in even indices:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            count += 1
    return count
```

This script provides a Python function called `count_upper` which achieves the task outlined in the original problem statement. It examines each character in the string `s`, only considering uppercase vowels ('AEIOU'), and increments a counter when these characters appear in even indices. The script successfully handles the test cases mentioned in the prompt and returns the correct values (1, 0, 0) for the example strings 'aBCdEf', 'abcdefg', and 'dBBE' respectively. 

Overall, the code is clean, efficient, and clearly documented, making it a robust solution for this problem.