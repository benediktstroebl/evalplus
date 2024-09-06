```python
def find_max(words):
    char_count = {}
    lexicographical_order = []
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        lexicographical_order.append([word, len(unique_chars)])
    max_unique_chars = max(char_count.values())
    max_entry = max(lexicographical_order, key=lambda x: x[1])
    return max_entry[0] if max_entry[1] == max_unique_chars else words[lexicographical_order.index(max_entry)]
```

The code employs a dictionary called `char_count` to tally the quantity of distinct characters present in each word. Subsequently, it arranges the words based on both their lexicographical order and the count of unique characters, storing them in the `lexicographical_order` list. By identifying the maximum count of unique characters across all words, the algorithm retrieves the word associated with this count. If multiple words share the highest unique character count, the script selects the word that was the earliest in lexicographical terms among those with the maximum count.