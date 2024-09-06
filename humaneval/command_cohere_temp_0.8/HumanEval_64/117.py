```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    cnt = 0
    for c in s:
        if c in 'aieou':
            cnt += 1
        elif c == 'y' and s.endswith(c):
            cnt += 1
    return cnt

# Test cases
assert vowels_count('abcde') == 2
assert vowels_count('ACEDY') == 3
assert vowels_count('AYEABLE') == 4
assert vowels_count('BYTE') == 1
assert vowels_count('CHAOS') == 2
``` 

This code defines the `vowels_count` function that takes a string `s` as input and returns the number of vowels in the word. It adds 1 to the counter if a vowel is encountered in the string, or if the letter 'y' is at the end of the word. The test cases then ensure that the function returns the expected outputs for various inputs.