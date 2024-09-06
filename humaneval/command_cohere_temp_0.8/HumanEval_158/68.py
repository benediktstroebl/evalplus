```python
def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_count = max(char_count.values())
    return char_count[lexicographically_first] if char_count[lexicographically_first] == max_count else lexicographically_first
```

The Python script provided solves the problem statement using a dictionary (`char_count`) to keep track of the unique characters in each word. It also uses a variable, `lexicographically_first`, to store the lexicographically smallest word with the maximum unique characters encountered so far. As the loop iterates through the input list of words, it updates the `char_count` dictionary and compares each word to the value stored in `lexicographically_first`. If a word has more unique characters and is lexicographically larger, the `lexicographically_first` variable is updated. After processing all words, the function returns the word that maximizes unique characters, following the criteria mentioned in the problem statement.