```python
def find_max(words):
    words.sort()
    max_char = 0
    result = None
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_char:
            max_char = len(unique_chars)
            result = word
    return result
```

The function `find_max` sorts the list of words lexicographically and then iterates through the list. For each word, it calculates the number of unique characters using a set and compares this count to the maximum seen so far. If the current word exceeds the maximum, the function stores this word and its count as the result to return. In the event of a tie in character count, the first one in lexicographical order will be the eventual return. 

This approach ensures that the result is returned in the fastest possible time complexity of O(n log n), and also uses the minimal amount of space due to the sorting step being O(n log n) and no extra space being utilised. 

This approach also makes sure that the function works in a deterministic way, making it easier to test and debug.