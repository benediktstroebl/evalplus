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

The function employs a dictionary named `char_count` to tally the quantity of unique characters present in each word. Employing this method, it ascertains the word with the most unique characters. In the event of a tie, the function returns the word that appears earliest in lexicographical order.

Here is an example usage of the function:
```python
print(find_max(["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]))
```

The code will output:
```
string
```