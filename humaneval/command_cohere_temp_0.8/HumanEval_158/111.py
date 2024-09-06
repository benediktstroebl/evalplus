```python
def find_max(words):
    char_count = {}
    max_count = 0
    max_word = None

    for word in words:
        unique_chars = set(word)
        count = len(unique_chars)
        if count > max_count:
            max_count = count
            max_word = word
        if count == max_count:
            if word < max_word:
                max_word = word

    return max_word
```

The code defines a function `find_max` that takes in a list of strings, specifically words. It counts the number of unique characters in each word using a dictionary and sets a maximum count. If multiple words have the same maximum count, it picks the one that appears first in lexicographical order. The code effectively solves the problem statement and returns the word with the most unique characters, considering lexicographical order when multiple words have the same maximum count. 

```python 
# Tests 
print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))
```

The example cases provided in the prompt will return the following outputs:
```
string
enam
aaaaaaa
``` 

These results demonstrate the function's ability to determine the word with the most unique characters and how it gives precedence to words that appear earlier in the lexicographical order when there are ties in character counts.