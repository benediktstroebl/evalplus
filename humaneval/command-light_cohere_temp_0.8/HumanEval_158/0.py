```python
def find_max(words):
    words.sort(max_count=lambda w: len(set(c for c in w)))
    return words[max_count]

# Tests
find_max(["name", "enam", "game"]) == "enam"
find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
```
This code defines a function `find_max` that takes a list of strings and returns the string that contains the maximum number of unique characters. The `max_count` function is a lambda function that creates a set of characters from each string in the list and then returns the length of this set, which is the maximum number of unique characters. 
The `find_max` function then returns the first string from the list that has this maximum count of unique characters.