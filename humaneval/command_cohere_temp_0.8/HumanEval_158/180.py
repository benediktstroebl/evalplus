```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: word for char, word in zip(unique_chars, [word])}
            max_char_word = word
        elif num_unique_chars == len(char_count) and word < char_count.values()[0]:
            max_char_word = word
    return max_char_word
```

The `find_max` function takes a list of words as input and calculates the number of unique characters in each word using a dictionary count. It then compares the count of unique characters in each word to determine the word with the highest count of unique characters. If there are multiple words with the same count, it selects the word that appears first in lexicographical order. The final result is the word with the maximum number of unique characters, considering the lexicographical order tie-breaker when necessary. 

This approach takes advantage of the dictionary's intrinsic ordering to compare values and select the smallest key when there is a tie in the values being counted.