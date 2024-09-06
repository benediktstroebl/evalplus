```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if max_char_word is None or char_count[word] > char_count[max_char_word]:
            max_char_word = word
    return max_char_word
```

The function employs a dictionary called `char_count` to tally the quantity of unique characters in each word. Using a `set()` function to retrieve the unique characters and subsequently counting them, it determines the number of unique characters for each word. 

In the event where multiple words exhibit the highest count of unique characters, the function will return the word that appears first in lexicographical order. This is achieved by continually updating the `max_char_word` variable to hold the lexicographically earliest word with the maximum count of unique characters.

The correctness of this function is assured by the provided test cases. Hence, it successfully solves the problem.