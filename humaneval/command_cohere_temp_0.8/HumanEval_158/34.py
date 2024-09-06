```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: num_unique_chars for char in unique_chars}
            max_char_word = word
        elif num_unique_chars == len(char_count) and word < max_char_word:
            max_char_word = word
    return max_char_word
```

The code defines a function `find_max` that solves the problem statement. It iterates through each word in the input list and counts the number of unique characters in the word using a set. It then compares this count to previously recorded counts, tracking the word with the most unique characters. If multiple words have the maximum count, the algorithm uses lexicographical order to select the earlier appearing word. The final result is the word with the most unique characters and the shortest lexicographical order among them.