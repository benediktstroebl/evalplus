```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] > char_count[max_char_word]:
            max_char_word = word
    return max_char_word
```

The function employs a dictionary named `char_count` to record the count of unique characters in each word. After iterating through the list of words, it compares the count of unique characters in each word with the count of the current maximum character word, and accordingly updates the maximum if a word with a higher count is encountered. Ultimately, the function returns the word with the most unique characters. 

This approach takes advantage of Python's dictionary manipulation capabilities to efficiently update and query data about each word's unique character count.