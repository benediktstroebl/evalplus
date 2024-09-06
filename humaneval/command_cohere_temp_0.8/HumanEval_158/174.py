```python
def find_max(words):
    words.sort()
    max_uniq = 0
    result = None
    for word in words:
        uniq = len(set(word))
        if uniq > max_uniq:
            max_uniq = uniq
            result = word
    return result
```

The function uses a straightforward iterative approach. Within the loop, it determines the unique character count for each word and compares this count to its previous maximum. When it detects a word with a higher unique character count, it updates the `result` variable to store that word. If multiple words have the same maximum unique character count, the loop will select the first one due to the sorted order of the input list.