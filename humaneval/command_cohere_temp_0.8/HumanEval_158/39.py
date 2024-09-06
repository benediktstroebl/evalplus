```python
def find_max(words):
    words.sort()
    max_uniq = 0
    result = None
    for word in words:
        current_uniq = len(set(word))
        if current_uniq > max_uniq:
            max_uniq = current_uniq
            result = word
    return result
```

The Python script uses a straightforward algorithm to solve the problem: it first sorts the list of words lexicographically, then loops through the sorted list, counting the number of unique characters in each word and updating the `result` and `max_uniq` accordingly. As the loop progresses, `result` will hold the word with the highest number of unique characters, and `max_uniq` will store the highest count. If you encounter any issues, feel free to ask!