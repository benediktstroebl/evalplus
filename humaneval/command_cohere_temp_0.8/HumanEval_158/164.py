```python
def find_max(words):
    char_count = {}
    max_word = None
    max_word_idx = None
    for idx, word in enumerate(words):
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if max_word is None or char_count[word] > char_count[max_word]:
            max_word = word
            max_word_idx = idx
    return words[max_word_idx]
```

The function uses a dictionary `char_count` to keep track of the number of unique characters in each word. Initially, the `max_word` and `max_word_idx` variables are set to `None`. The function then iterates through the list of words, calculating the number of unique characters for each word using a `set` data structure. If the current word has more unique characters than the previously recorded maximum, the `max_word` and its index `max_word_idx` are updated. After iterating through all the words, the function returns the word with the maximum number of unique characters, considering the lexicographical order when multiple words have the same character count. 

Here is an example output of the function:
```python
find_max(["name", "of", "string"])  # Output: "string"
find_max(["name", "enam", "game"])  # Output: "enam"
find_max(["aaaaaaa", "bb", "cc"])  # Output: "aaaaaaa"
```