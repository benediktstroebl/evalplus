```python
def find_max(words):
    char_count = {}
    max_count = 0
    max_word = None

    for word in words:
        unique_chars = set(word)
        current_count = len(unique_chars)

        if current_count > max_count:
            max_count = current_count
            max_word = word

        if current_ count < max_count:
            continue

        if current_count == max_count:
            if word < max_word:
                max_word = word

    return max_word
```

The `find_max` function takes a list of words as input and iterates through each word, using a dictionary to keep track of the unique characters and their counts. It then compares the unique character counts of each word, initially storing the word with the highest count and subsequently updating the maximum if a word has an equal count but appears earlier in lexicographical order. The result is the word with the most unique characters while adhering to the lexicographical criterion in cases of a tie. 

This approach ensures efficiency and simplicity in solving the challenge posed, achieving a time complexity of `O(n)` due to the single pass through the list of words.