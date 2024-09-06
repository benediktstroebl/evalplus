```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Returns the number of vowels in a string s,
       considering 'y' a vowel only at the end of the word.
    """
    # your code here
    total = 0
    for char in s:
        if char in 'aieou':
            total += 1
        elif char == 'y' and s[-1] == 'y':
            total += 1
    return total
```

This Python script defines a function called `vowels_count` that takes a string as input and counts the number of vowels in the string. 

In this case, 'y' is also considered a vowel only if it is at the end of the given word. The function iterates through each character in the string, counting the number of vowels and adding them to the total count. The function then returns the total count of vowels.