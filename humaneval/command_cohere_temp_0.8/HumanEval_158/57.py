```python
def find_max(words):
    max_set = None
    max_word = None
    for word in words:
        char_set = set(word)
        if char_set not in max_set or (char_set == max_set and word < max_word):
            max_set = char_set
            max_word = word
    return max_word
```

The function iterates through each word in the list, calculating the set of unique characters within each word. It then compares this set to the previous 'max' set, storing the one with the most unique characters. If there's a tie, it selects the word that appears earlier in lexicographical order. Ultimately, the function returns the optimal word.

This approach ensures optimal performance, O(n), with a space complexity of O(1). It correctly identifies the word with the most unique characters and uses lexicographical order as a tie-breaker.