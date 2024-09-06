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

The function `find_max` takes a list of words as input and returns the word with the highest count of unique characters. If multiple words have the highest count of unique characters, the result is the word that appears first in lexicographical order.

This approach uses a dictionary to count the number of unique characters in each word. The dictionary stores the character as the key and its count as the value. After counting the unique characters for each word, the function compares the counts to determine the word with the highest count and the right lexicographical order.