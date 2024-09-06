```python
def find_max(words):
    words.sort()
    max_set = set()
    for word in words:
        char_set = set(word)
        if len(char_set) > len(max_set):
            max_set = char_set
    return words[max_set == max_set].strip("\n")
```

The function first sorts the list of words lexicographically. It then iterates through the list, creating a set of unique characters for each word. The sets are compared to each other, and the index of the word whose character set is the largest is stored. Finally, the function returns the word corresponding to the index of the largest character set. 

This approach takes advantage of sets' uniqueness property to compare the uniqueness of characters in each word efficiently. Additionally, sorting the words beforehand ensures a more efficient iteration through the list.