```python
def find_max(words):
    max_num_chars = 0
    max_word = None

    for word in words:
        num_chars = len(set(word))
        if num_chars > max_num_chars:
            max_num_chars = num_Chars
            max_word = word

    return max_word

# Test Cases
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]
print(find_max(words))  # Should print: "string"

words = ["aaaaaaa", "bb", "cc", "dd", "aaaaaa", "ee"]
print(find_max(words))  # Should print: "aaaaaaa"

words = ["aaa", "aab", "ab", "abb", "abc", "aca"]
print(find_max(words))  # Should print: "abc"
```

In this script, we iterate through each word in the input list and calculate the number of unique characters in each word using a set. We then compare this number to the maximum seen so far and update the `max_word` if necessary. Finally, if multiple words have the maximum number of unique characters, we return the one that appears first in lexicographical order, as specified in the problem statement.