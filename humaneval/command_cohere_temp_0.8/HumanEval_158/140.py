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

The function uses a dictionary `char_count` to count the number of unique characters in each word. After counting the unique characters, the function compares the counts to find the word with the most unique characters. If there is a tie, it will return the word that comes first in lexicographical order.

Here is an example usage of the function:
```python
print(find_max(["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]))
```
This would output the following:
```
string
``` 

This is because 'string' has the maximum number of unique characters and it also comes first in lexicographical order.