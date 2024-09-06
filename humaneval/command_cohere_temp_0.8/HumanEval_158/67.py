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

The code defines a function `find_max` that takes in a list of words and returns the word with the highest count of unique characters, considering the lexicographical order when multiple words have the same count.

The algorithm uses a dictionary, `char_count`, to track the count of unique characters in each word. For each word, it calculates the count of unique characters and checks if this count is higher than the counts of other words. If it is, the dictionary `char_count` is updated with the new word. If the count is the same but the word is lexicographically smaller, it also replaces the max_char_word. Finally, the function returns the `max_char_word`.