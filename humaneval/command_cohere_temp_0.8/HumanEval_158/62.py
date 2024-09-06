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
    
    for char_count_key, word_list in char_count.items():
        if max_word is None or len(word_list) > len(max_word_list):
            max_word_list = word_list
            max_word_index = char_count_key
            max_word = sorted(word_list)[0][0]
    
    return max_word
```

The Python script provided solves the problem statement by using a dictionary `char_count` to keep track of words that have a certain number of unique characters. It then iterates over each word in the input list, determining its unique character count and storing it with its index in `char_count`. After collecting this data, the script sorts the lists of words with the same count of unique characters by lexicographical order and picks the list with the maximum length, assuming it indicates the word with the most unique characters. The word is then extracted and returned.