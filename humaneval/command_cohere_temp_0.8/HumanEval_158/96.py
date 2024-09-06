```python
def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if max_word is None or char_count[word] > char_count[max_word]:
            max_word = word
    return max_word
```

The function uses a dictionary `char_count` to count the number of unique characters in each word. After counting the unique characters, the function compares the counts to find the word with the most unique characters. If multiple words have the maximum count, the function returns the one that comes first in lexicographical order.

Here is a simpler approach that solves the problem:
```python
def find_max(words):
    max_word = max(words, key=len)
    unique = set()
    for char in max_word:
        if char in unique:
            return max_word
        unique.add(char)
    return max_word
```

This approach takes advantage of the fact that if a word has the maximum length, it must also have the maximum number of unique characters. Therefore, it is enough to just find the word with the maximum length, and then check if each character in this word is unique.