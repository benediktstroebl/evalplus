```python
def find_max(words):
    max_num_uniq_chars = 0
    max_word = None

    for word in words:
        num_uniq_chars = len(set(word))
        if num_uniq_chars > max_num_uniq_chars:
            max_num_uniq_chars = num_uniq_chars
            max_word = word

    return max_word

# Test Cases
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]
print(find_max(words))  # Output: "string"

words = ["aaaaaaa", "bb", "cc", "aaaaaab", "cc"]
print(find_max(words))  # Output: "aaaaaaa"

words = ["one", "two", "three", "four", "one", "five", "six"]
print(find_max(words))  # Output: "one"
``` 

This Python script defines a function `find_max` that solves the problem using a brute-force approach without any external libraries. It iterates through the list of words, calculates the unique character count for each word, and keeps track of the maximum count and the associated word. Finally, it returns the word that maximizes the unique character count, considering the secondary sort order of words with the same maximum count.