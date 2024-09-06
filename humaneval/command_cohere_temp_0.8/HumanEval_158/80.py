```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: word for char, word in zip(unique_chars, [word])}
            max_char_word = word
        elif num_unique_chars == len(char_count) and word < char_count.values()[0]:
            max_char_word = word
    return max_char_word
```

The code defines a function `find_max` that takes in a list of strings, `words`. The function aims to find the word with the maximum number of unique characters among the list and returns it. If there are multiple words with the same maximum number of unique characters, the function returns the one that appears first in lexicographical order.

The approach is to maintain a dictionary, `char_count`, that maps each character to the word it belongs to. If a word has more unique characters than any previous word, the `char_count` dictionary is updated to reflect this. If there is a tie in the number of unique characters between two words, the dictionary is used to compare and the word that appears first in lexicographical order is considered the winner. Finally, the function returns the best word found.