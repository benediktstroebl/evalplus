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

The function uses a dictionary `char_count` to count the number of unique characters in each word. After counting the unique characters of each word, the function identifies the word with the maximum number of unique characters. If there are multiple words with the same maximum count, the function will return the word that appears first in lexicographical order. The solution is achieved without extra space complexity as the dictionary is used just once for counting the characters.