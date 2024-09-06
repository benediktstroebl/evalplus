```python
def count_consonants(word):
    """
    Counts the number of consonants in a word.
    A consonant is a letter that is not a vowel (case-insensitive)
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return len([c for c in word.lower() if c not in vowels and c != ' '])

def select_words(s, n):
    """
    Returns a list of words from string s that contain exactly n consonants, in order they appear in the string s
    """
    words = s.split(' ')
    result = []

    for word in words:
        if count_consonants(word) == n:
            result.append(word)

    return result if result else ['']

# Example usage
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
```

This script utilizes the `count_consonants` function to tally the number of consonants in a given word, defining a consonant as any letter that is not a vowel or a space. This function helps define the logic used by the `select_words` function, which is designed to filter and return words from a given string that contain a specific number of consonants. The `select_words` function initially splits the string into a list of words, then examines each word to determine if it matches the desired consonant count, adding qualifying words to the `result` list. The final output is a list of words from the provided string that each contain precisely the specified number of consonants.