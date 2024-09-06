```python
def find_max(words):
    char_count = {}
    max_word = None
    max_word_index = None
    
    for index, word in enumerate(words):
        unique_chars = set(word)
        num_unique_chars = len(unique_chars)
        
        if num_unique_chars not in char_count:
            char_count[num_unique_chars] = []
        
        char_count[num_unique_chars].append((word, index))
    
    for char_count_key, word_entries in char_count.items():
        sorted_word_entries = sorted(word_entries)
        if max_word is None or max_word_index == sorted_word_entries[0][1]:
            max_word = sorted_word_entries[0][0]
            max_word_index = sorted_word_entries[0][1]
        elif max_word_index > sorted_word_entries[0][1]:
            max_word = sorted_word_entries[0][0]
            max_word_index = sorted_word_entries[0][1]
    
    return max_word
```

The algorithm to solve the problem involves using a dictionary `char_count` that maps the number of unique characters to a list of words that have that number of unique characters. We iterate through the list of words, determining the number of unique characters for each word and updating the `char_count` dictionary. Then, we iterate through the dictionary and sort the words based on their appearance count. We update the `max_word` and `max_word_index` accordingly. Finally, we return the `max_word` found.