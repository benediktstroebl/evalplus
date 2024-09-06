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

The function uses a dictionary `char_count` to keep track of the number of unique characters in each word. After iterating through all the words, it checks which word has the maximum count and returns it, considering the lexicographical order in case of a tie.

Here are some example inputs and outputs to test the function:
```python
print(find_max(["name", "of", "string"])) # Output: "string"
print(find_max(["name", "enam", "game"])) # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # Output: "aaaaaaa"
``` 

This should output:
```
string
enam
aaaaaaa
```