Here's a Python script that defines a function `select_words()` to solve the problem as described in the code block:
```python
def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    words = s.split()
    result = [word for word in words if len(word) >= n and len(set(word).intersection(consonants)) == n]
    return result if result else []
```

This script assumes that the input string `s` contains only letters and spaces, and the dictionary `consonants` contains all possible consonants in the English alphabet. The function first splits the input string into a list of words, then it iterates over each word, checks if its length is greater than or equal to `n`, and counts the number of consonants in the word using set subtraction (`set(word).intersection(consonants)`). If this count is exactly `n`, the word is added to the `result` list. Finally, the function returns this list of words with exactly `n` consonants, or an empty list if no such words are found in the input string.

To handle the edge case of an empty input string, the code includes a protective clause `return result if result else []` to avoid any potential `IndexError` from list slicing when `s` is empty. 

You can test this function by calling `select_words()` with different input strings and values of `n` to verify that it produces the desired output as per the problem description.