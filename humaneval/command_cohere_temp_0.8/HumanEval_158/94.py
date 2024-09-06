```python
def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_char_word = min(char_count, key=char_count.get)
    return lexicographically_first if char_count[lexicographically_first] == char_count[max_char_word] else max_char_word
``` 

The `find_max` function solves the problem by first, creating a dictionary, `char_count`, that stores the number of unique characters in each word. It then identifies the word with the highest count of unique characters among these and returns it, maintaining the lexicographical rule if there's a tie. 

The use of `min(char_count, key=char_count.get)` is a neat trick to identify the key with the maximum value, as it sorts the keys of `char_count` descending by their values and selects the first one, which corresponds to the word with the highest count.