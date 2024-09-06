Here's the Python code to solve the problem:
```python
def count_upper(s):
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This script defines the `count_upper()` function, which takes a string `s` as input and returns the number of uppercase vowels in even indices of that string. It utilizes a set called `upper_vowels` to efficiently check if the vowel is uppercase, and iterates through the string at twice the speed, checking for vowels in even indices. 

To ensure the functionality, here are corresponding test cases:
```python
def test_count_upper():
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
    assert count_upper('Aaaa') == 0
    assert count_upper('Eeeeee') == 1
    assert count_upper('Iiii') == 1
    assert count_upper('Oooooo') == 1
    assert count_upper('Uuuuuuu') == 1
```

Ensure that you run these tests to validate the correctness of the `count_upper()` function.  This solution is efficient and should efficiently handle any string input.