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
```

This Python script defines a function vowels_count that takes a string s as input and returns the number of vowels in the string. The function counts the number of vowels ('a', 'e', 'i', 'o', 'u') and the letter 'y' when it appears at the end of the word, updating a counter variable cnt accordingly. It then returns the value of cnt, which represents the number of vowels in the input string.