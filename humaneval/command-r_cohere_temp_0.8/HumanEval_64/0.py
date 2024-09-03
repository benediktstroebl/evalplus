```python
FIX = """
Add more test cases as needed.
"""

def vowels_count(word):
    """
    Count the number of vowels in a word. 'Y' is considered a vowel only if it's the last letter.

    Parameters:
        word (str): A string representing a word.

    Returns:
        int: Number of vowels in the word.
    """
    vowels = "aeiou"
    count = 0

    if len(word) > 0:
        if word[-1] == 'y':
            word = word[:-1]

        for char in word.lower():
            if char in vowels:
                count += 1

    return count
```