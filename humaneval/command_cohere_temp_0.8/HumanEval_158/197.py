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

The function uses a set data structure to count the unique characters in each word. The lexicographical order is used to break the tie when the count of unique characters is the same. The function returns the maximum word according to the rules mentioned in the prompt. You can test the function by calling it with various input lists to ensure its behavior aligns with the problem statement.  This approach offers a concise and efficient solution by utilizing sets and tracking maximum unique character counts, ultimately leading to the optimal result.