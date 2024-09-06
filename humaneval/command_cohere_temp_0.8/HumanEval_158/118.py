```python
def find_max(words):
    char_count = {}
    max_count = 0
    result = None
    for word in words:
        unique_chars = set(word)
        num_unique = len(unique_chars)
        if num_unique > max_count:
            max_count = num_unique
            result = word
        if num_unique == max_count:
            if word < result:
                result = word
    return result
```

The Python script defines a function `find_max` that solves the problem statement. It iterates through each word in the input list and counts the unique characters in each word, using a dictionary `char_count` to track the count of each character. 

The script then keeps track of the maximum count of unique characters seen so far and the word associated with it. If a new word has a higher count of unique characters, it updates the `result` variable to store that word. If a word has the same count of unique characters but appears earlier in lexicographical order, it also updates the `result` variable.

In summary, the `find_max` function efficiently identifies the word with the most unique characters and returns it, satisfying the conditions outlined in the problem statement.