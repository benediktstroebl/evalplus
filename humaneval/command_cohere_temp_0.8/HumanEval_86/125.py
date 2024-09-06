Here's a Python script that solves the anti-shuffle problem:
```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        char_array = list(word)
        char_array.sort()
        new_word = ''.join(char_array)
        new_word_array.append(new_word)
    return ' '.join(new_word_array)
```

This script takes a string `s` as input and returns an ordered version of it, where all the words are replaced by a new word where all the characters are arranged in ascending order based on their ASCII value. The script first splits the input string into an array of words and then sorts the characters in each word. The sorted characters are then joined to form a new word, which is added to the `new_word_array`. Finally, the script returns a space-separated string of all the new words in the same order as the original words.

Here is an example:
```python
print(anti_shuffle("Hello World!!!")) # Output: "Hello !!!Wdlor"
```

This will output: "Hello !!!Wdlor" where the words are ordered alphabetically.