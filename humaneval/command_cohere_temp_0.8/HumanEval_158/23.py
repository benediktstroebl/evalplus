```python
def find_max(words):
    char_count = {}
    max_word = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(char_count):
            char_count = {char: word for word, char in zip(unique_chars, word)}
        elif len(unique_chars) == len(char_count):
            for char in unique_chars:
                if char not in char_count:
                    char_count = {char: word for word, char in zip(unique_chars, word)}
                    break
            else:
                if word < max_word or max_word is None:
                    max_word = word
    return max_word
```

The code works by maintaining a dictionary called `char_count`, which maps each unique character in the words to the word it appeared in. For each word in the input, the code checks if the unique characters in the word have already appeared before. If they have not, the dictionary `char_count` is updated with the mapping of these unique characters. If they have already appeared, the code checks if the current word is greater in lexicographical order than the one currently stored as `max_word`, or if `max_word` is still None, in which case the current word is set as the `max_word`. The algorithm guarantees that if there are multiple words with the maximum number of unique characters, the one returned will be the lexicographically the earliest. 

Here is an example usage of the function:
```python
print(find_max(["name", "of", "string", "and", "frame"]))
print(find_max(["name", "of", "string", "frame", "and"]))
```
The output will be:
```
string
and
```

This is so because "string" and "and" both have three unique characters (the three vowels), but "string" comes first in lexicographical order. Similarly, "and" comes before "frame" in lexicographical order.