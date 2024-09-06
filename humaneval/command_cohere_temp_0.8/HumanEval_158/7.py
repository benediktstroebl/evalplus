```python
def find_max(words):
    max_count = 0
    max_word = None
    for word in words:
        unique = set(word)
        count = len(unique)
        if count > max_count:
            max_count = count
            max_word = word
    return max_word
```

The function uses a simple algorithm that iterates through the list of words, and for each word, it calculates the number of unique characters in the word by converting it into a set and then getting the length of this set with `len(set(word))`. We store the word that gives the maximum count in the `max_word` variable.

This solution effectively selects the word with the most unique characters and fulfills the requirement of selecting the lexicographically earliest word in case of a tie. 

This approach has a time complexity of `O(n)` since it requires iterating through the list of words once, making it efficient for moderate-sized inputs.