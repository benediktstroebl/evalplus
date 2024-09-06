```python
def find_max(words):
    words.sort()
    max_set = set()
    for word in words:
        char_set = set(word)
        if len(char_set) > len(max_set):
            max_set = char_set
    return words[max_set == max_set][0]
```

The function first sorts the list of words lexicographically. It then uses a maximum set of unique characters approached by using a `for` loop that traverses the sorted list and compares the unique characters in each word. The maximum set of unique characters is stored in the `max_set` variable. Finally, the function returns the first word whose unique characters make up the `max_set` value, which ensures the word has the maximum number of unique characters.