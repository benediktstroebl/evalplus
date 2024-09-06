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

The function uses a dictionary `char_count` to count the number of unique characters in each word. After counting the unique characters, the function compares the counts to find the word with the most unique characters. If there is a tie, it defaults to the lexicographically earlier word.

#### Testing
```python
def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max([["a", "b"], ["c", "d"], ["e", "f"]]) == "e"
```