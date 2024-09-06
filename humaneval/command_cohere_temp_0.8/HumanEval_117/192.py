Here's a Python script that defines a function `select_words` to solve the problem:
```python
def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    words = s.split() 
    result = [word for word in words if len(word) >= 3 and len(set(word).intersection(consonants)) == n]
    return result if result else []
```

The `select_words` function splits the input string into a list of words and then iterates over each word. It calculates the count of consonants in the word using a built-in Python set and a string of all consonants. It checks if the count is equal to the given number `n` and the word length is greater than 2 (to avoid single letters being considered). The function then returns a list of all eligible words. If no words match the criteria, it returns an empty list.

This solution has a time complexity of O(n ^ 2) due to the nested loop structure, but it can be optimized to O(n) by leveraging the capabilities of a language model like Command, which can directly extract words based on the consonant criteria. If you'd like, I can provide an example of how to do this with a language model like Command.