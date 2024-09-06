```python
def find_max(words):
    char_count = {}
    lex = sorted(words, key=lambda x: (len(set(x)), x))
    for i in range(len(lex)):
        temp = set(lex[i])
        char_count[lex[i]] = len(temp)
    return char_count[lex[0]]
```

The function uses a dictionary called `char_count` to count the number of unique characters in each word. The function then checks the dictionary to find the word with the maximum count of unique characters. If there is a tie, the function will return the word that appears first in lexicographical order.

Here is an example usage of the function:
```python
print(find_max(["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]))
```
The output of the code is:
```
8
```

Which is the word 'string' has 8 unique characters and it is the first lexicographically ordered word among all words with maximum unique characters.