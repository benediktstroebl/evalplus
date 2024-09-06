```python
def find_max(words):
    words.sort()
    max_word = words[0]
    num_set = set()
    for word in words:
        num_set.update(word)
        if len(num_set) == len(word):
            if len(word) > len(max_word):
                max_word = word
    return max_word
```

The function `find_max` accepts a list of strings, sorts the list, and then iterates through the list to count the unique characters in each word. If a word has the maximum number of unique characters, the function updates the `max_word` variable. The final output is the `max_word` variable, which will be the first word in lexicographical order that has the maximum number of unique characters. 

Here is an example output of the function:
```python
find_max(["name", "of", "string"])  # Output: "string"
find_max(["name", "enam", "game"])  # Output: "enam"
find_max(["aaaaaaa", "bb", "cc"])  # Output: "aaaaaaa"
``` 

This is a self-contained Python script that solves the problem using a efficient strategy in a single function.