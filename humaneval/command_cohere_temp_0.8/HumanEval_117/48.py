```python
def count_consonants(word):
    return sum(1 for char in word if char.isalpha())

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The `count_consonants` helper function calculates the total count of consonants in a given word. It iterates through each character in the word and checks if the character is alpha (a letter), incrementing a counter when true. 

The `select_words` function takes the input string `s` and integer `n`, and identifies all words in `s` containing exactly `n` consonants. It splits the input string into a list of words, and then uses a list comprehension to filter this list, only including words with a consonant count equal to `n`. 

The script returns a list with all these selected words, ordered as they appear in the original string. This list is then returned by the function.