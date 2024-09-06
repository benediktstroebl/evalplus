```python
def find_max(words):
    max_uniq = 0
    max_word = None
    for word in words:
        current_uniq = len(set(word))
        if current_uniq > max_uniq:
            max_uniq = current_uniq
            max_word = word
    return max_word
```

The function `find_max` uses a loop to iterate through each word in the list and determine the number of unique characters in each word. If the current word has more unique characters than the previous maximum, the function updates both the maximum number of unique characters and the corresponding word.

In the event of a tie between multiple words having the maximum number of unique characters, the script elects to return the word that appears earliest in lexicographical order.