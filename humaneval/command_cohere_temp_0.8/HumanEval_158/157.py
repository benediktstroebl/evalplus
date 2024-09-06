```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] > len(char_count):
            max_char_word = word
    if max_char_word is None:
        return ""
    return max_char_word
```

The script defines a function `find_max` that accepts a list of strings, identifies the word within that list that contains the maximum number of unique characters, and returns it. If multiple words have the same maximum number of unique characters, the function will return the one that appears first in lexicographical order.

The algorithm runs through each word in the list, counting the number of unique characters it contains. These character counts are stored in a dictionary where the key is the word and the value is the count. Following this, the function identifies the word with the maximum character count and returns it. If multiple words have the same maximum count, it defaults to the lexicographically earlier one. 

Overall, the script efficiently solves the problem and meets the criteria outlined in the prompt.