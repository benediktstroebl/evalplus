```python
def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(char_count):
            char_count = {char: word for word, char in unique_chars.items()}
        if max_word is None or len(char_count) < len(max_word):
            max_word = word
    return max_word
```

The function uses a dictionary `char_count` to count the number of unique characters in each word. Initially, the count is computed by creating a set of unique characters present in the word. If the unique character count exceeds the previous maximum, the dictionary is updated with the new word and its corresponding characters. Furthermore, the loop iterates through the words in lexicographical order to ensure that if multiple words have the same maximum unique character count, the first one will be selected as per the prompt's instructions. 

Here is a quicker solution:
```python
import collections

def find_max(words):
    char_counts = collections.Counter(word)
    return min(words, key=char_counts.get)
```
This solution uses the third-party `collections` module specifically designed for Python to provide various containers with unique functionalities. The `collections.Counter` class is used to create `char_counts`, a dictionary-like object that stores the word-character associations. Subsequently, the `min` function is used to identify the word with the highest number of unique characters from the `char_counts` object, with the `key` argument specifying that the `get` method of `char_counts` should be used as the comparison key.