```python
def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(char_count):
            char_count = {char: word for word, char in zip(unique_chars, word)}
        elif len(unique_chars) == len(char_count):
            for char in unique_chars:
                if char not in char_count:
                    char_count = {char: word for word, char in zip(unique_chars, word)}
                    break
            else:
                if word < max_word or max_word is None:
                    max_word = word
    return max_word
```

The Python script defines a function `find_max`, which takes in a list of strings (words) as input. It aims to find the word with the maximum number of unique characters among the list while using a dictionary to keep track of the counts of characters. If there's a tie in the number of unique characters, it uses lexicographical order to favor the word that comes earliest in the alphabet. The script works through the list of words, updating the dictionary as it goes, ultimately returning the word that maximizes the number of unique characters.