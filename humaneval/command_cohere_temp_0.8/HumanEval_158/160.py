```python
def find_max(words):
    char_count = {}
    max_word = None
    max_char_count = 0
    
    for word in words:
        unique_chars = set(word)
        current_char_count = len(unique_chars)
        
        if current_char_count > max_char_count:
            max_char_count = current_char_count
            max_word = word
        elif current_char_count == max_char_count:
            if word < max_word:
                max_word = word
    
    return max_word
```

The function `find_max` performs the following steps:
1. It initializes a dictionary `char_count` to keep track of the number of occurrences of each character in the words.
2. It assigns `None` to the variable `max_word` and `0` to `max_char_count` to initialize the variables.
3. It iterates through each word in the input list.
4. For each word, it calculates the number of unique characters by converting the word into a set and counting the number of elements in the set.
5. If the current word has more unique characters than the previously recorded maximum, it updates `max_char_count` and `max_word`.
6. If the current word has the same number of unique characters as the previous maximum, it checks if the current word appears before the current max_word in lexicographical order. If so, it updates `max_word`.
7. After processing all words, it returns the final `max_word`.

The expected outputs are:
```
find_max(["name", "of", "string"]) == "string"
find_max(["name", "enam", "game"]) == "enam"
find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
```

The provided solution works correctly for words containing characters of different counts, as shown in the test cases.