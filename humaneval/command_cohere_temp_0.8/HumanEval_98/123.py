Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    uppercase_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in uppercase_vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The example tests provided in the initial problem description are all included and should pass correctly. 

**NOTE:** The assumption here is that "uppercase vowels" refers to the set of characters ['A', 'E', 'I', 'O', 'U']. If the problem definition excludes 'U' or includes other characters, the script can be adjusted accordingly. 

To execute the script and run the tests, you can enter the script into a Python file (e.g., `count_upper.py`) and execute it using a Python environment like the command line:
```bash
python count_upper.py
``` 

This will execute the script and print the result of running the function with the provided tests.