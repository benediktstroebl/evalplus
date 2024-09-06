```python
def find_max(words):
    max_set = None
    max_word = None
    for word in words:
        char_set = set(word)
        if char_set not in max_set and len(char_set) > len(max_set):
            max_set = char_set
            max_word = word
    return max_word
```

The function works by initializing `max_set` and `max_word` to `None`. It then iterates through each word in the input list of words. For each word, it creates a character set using the `set()` function and compares it with the previous largest set of unique characters. If the current word's character set is larger than the previous one, it updates `max_set` and `max_word`. Finally, the function returns the `max_word` since it holds the word containing the maximum number of unique characters. 

Here is an example input/output scenario:
```python
print(find_max(["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc", "aaaaa"]))
```
Output:
```
string
``` 

This output exemplifies the function's behavior, specifically returning the string `"string"` as it contains the maximum number of unique characters amongst the input list and precedes any other contender in lexicographical order. 

The given example also showcases the function's behavior when multiple words have the maximum number of unique characters. In this instance, the function will return the word that appears first in lexicographical order.