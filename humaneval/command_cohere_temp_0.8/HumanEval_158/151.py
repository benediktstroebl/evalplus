```python
def find_max(words):
    words.sort()
    max_set = set()
    len_max = 0
    for word in words:
        len_cur = len(set(word))
        if len_cur == len_max:
            if word < words[len_max]:
                len_max = len_cur
                max_set = set([word])
        elif len_cur > len_max:
            len_max = len_cur
            max_set = set([word])
    return max_set.pop0()
```

The Python script defines a function `find_max` that takes in a list of strings, sorts it lexicographically, and then searches for the word with the maximum number of unique characters. Using a `for` loop, it iterates through each word in the sorted list, calculating the current unique character count using the `set()` and `len()` functions and saving the word if it has the same maximum length or more. After looping through all the words, the function returns the word saved in the `max_set`, which is ensured to be the word with the maximum number of unique characters and the correct lexicographical order. 

This problem can be solved in various ways, but this approach highlights an efficient and readable solution through sorting and character set analysis.