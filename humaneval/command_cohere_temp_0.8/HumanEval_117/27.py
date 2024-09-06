Here's a Python script that defines a function `select_words()` to solve the problem you've outlined:
```python
def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    words = s.split()
    result = [word for word in words if len(word) >= n and sum(1 for char in word if char in consonants) == n]
    return result if result else []
```

This script splits the input string into a list of words, counts the number of consonants in each word, and then filters the words to include only those with exactly `n` consonants, returning them in the order they appear in the original string.

Let's break down the code step by step:
1. **Consonant Generator**: The string `consonants` contains all possible consonants in English language, excluding vowels. This is used to efficiently check whether a character is a consonant.
2. **Splitting the String into Words**: The line `words = s.split()` splits the input string `s` using spaces as separators, converting the string into a list of words.
3. **Word Checking and Filtering**: The list comprehension `result = [word for word in words if len(word) >= n and sum(1 for char in word if char in consonants) == n]` checks each word in the list:
    - `len(word) >= n`: Checks if the word is long enough to potentially have n consonants. This is to avoid checking consonants of very short words.
    - `sum(1 for char in word if char in consonants) == n`: Counts the number of consonants in the word. This is done using a generator expression, an optimized way to count occurrences.

The line `return result if result else []` ensures that if no words match the criteria, an empty list is returned. 

Overall, the code efficiently identifies words in the input string with exactly n consonants and returns them in the order they appear.