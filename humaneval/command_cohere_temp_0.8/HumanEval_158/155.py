```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        if num_unique_chars > len(char_count):
            char_count = {char: num_unique_chars for char, num_chars in zip(word, range(num_unique_chars)) }
            max_char_word = word
        elif num_unique_chars == len(char_count) and word < max_char_word:
            max_char_word = word
    return max_char_word
```

This code defines a function `find_max` that solves the problem as described in the prompt. It takes a list of strings `words` as input and returns the word with the maximum number of unique characters, considering lexicographical order. 

The approach involves maintaining a count of unique characters encountered so far and updating it for each word. Once the count is maxed out for a word, that word is selected as the answer. If multiple words have the same max count, the lexicographically earliest one is returned.

The expected outputs for the provided test cases are:
- `find_max(["name", "of", "string"]) == "string"`
- `find_max(["name", "enam", "game"]) == "enam"`
- `find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"` 

The approach is not the most efficient for large inputs because it needs to iterate over the input list and create a dictionary of character counts every time. However, for small inputs like these, it's manageable and provides the desired result. 

Lastly, this code showcases basic variable assignments, dictionary creation, set operations, and conditional comparisons in Python, making it a simple yet functional solving of the problem.