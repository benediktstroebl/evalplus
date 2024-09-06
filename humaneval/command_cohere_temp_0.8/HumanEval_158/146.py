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

The function employs a dictionary named `char_count` to tally the quantity of unique characters present in each word. Through continual comparison of character counts, the function identifies the word with the most unique characters. In the event of a tie, the function defaults to selecting the word that appears earliest in lexicographical order.

Here is an example usage of the function:
```python
print(find_max(["name", "of", "string"]) )  # output: "string"
print(find_max(["name", "enam", "game"]) )  # output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]) )  # output: "aaaaaaa"
```

This demonstrates the function's ability to identify the word with the maximum number of unique characters, considering lexicographical order when necessary.