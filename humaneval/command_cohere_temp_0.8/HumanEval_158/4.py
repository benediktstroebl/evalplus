```python
def find_max(words):
    words.sort()
    max_word = words[0]
    num_unique = len(set(max_word))
    for word in words:
        current_num_unique = len(set(word))
        if current_num_unique > num_unique:
            max_word = word
            num_unique = current_num_unique
    return max_word
```

This Python script defines a function called `find_max`, which takes in a list of words as input. The function sorts the input list in lexicographical order and then iterates through each word, counting the number of unique characters in each word using the `set` function. It keeps track of both the word with the highest count of unique characters and the current count of unique characters while comparing them with the previous values. This approach ensures that the function correctly returns the word with the most unique characters along with handling cases where multiple words have the same maximum count of unique characters. 

The given example tests will yield the following results:
```
find_max(["name", "of", "string"]) == "string"
find_max(["name", "enam", "game"]) == "enam"
find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
```

The script fully meets the problem requirements, providing an efficient and accurate solution. Let me know if further clarification is needed or if you'd like to tackle more related problems!