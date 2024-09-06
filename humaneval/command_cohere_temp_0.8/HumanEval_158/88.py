```python
def find_max(words):
    words.sort()
    max_word = words[0]
    num_unique = len(set(max_word))
    for word in words:
        current_num_unique = len(set(word))
        if current_num_unique > num_unique:
            max_word = word
            num_unique = current_num_unique
    return max_word
```

This script sorts the list of words lexicographically and then loops through the sorted list to find the word with the maximum number of unique characters. The result is the word that occurs first in lexicographical order and maximizes the number of unique characters.