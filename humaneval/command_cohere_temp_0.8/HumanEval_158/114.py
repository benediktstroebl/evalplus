```python
def find_max(words):
    char_count = {}
    lexic_front = []
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] == max(char_count.values()):
            lexic_front.append(word)
            
    return lexic_front[0] if lexic_front else None
```

The Python script defines a function `find_max` that solves the problem statement using the following approach:
1. Initialize an empty dictionary `char_count` to keep track of the count of unique characters in each word.
2. Create an empty list `lexic_front` to store words that have the maximum count of unique characters. This list ensures we can retrieve the lexicographically smallest word with the maximum character count.
3. Iterate through each word in the input list `words`.
4. For each word, calculate the count of unique characters by converting the word into a set and getting its size.
5. Update the `char_count` dictionary with the calculated unique character count for the word.
6. If the unique character count is equal to the maximum count among all words, add the word to the `lexic_front` list. This ensures we track the lexicographically smallest word with the maximum unique character count.
7. After processing all words, if the `lexic_front` list is not empty, return the first word from the list. If the list is empty, return `None` since there are no words in the input.

This approach efficiently solves the problem by first identifying all words with the maximum unique character count and then returning the lexicographically smallest among them.