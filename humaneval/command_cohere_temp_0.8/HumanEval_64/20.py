```python
 FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count

# Add your test cases below
print(vowels_count("abcde"))
print(vowels_count("ACEDY"))
print(vowels_count("Hello"))
print(vowels_count("Pie"))

```
This code defines a function called `vowels_count` that takes a string as input and counts the number of vowels in the string, with the exception of 'y' unless it's at the end of the word. The code then prints the result of the function for several test cases.