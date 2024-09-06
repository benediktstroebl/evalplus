```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using space as the delimiter, and then iterates through each word. For each word, it sorts the characters based on their ASCII values and concatenates them to create a new sorted word. These sorted words are then reassembled with spaces in between to form the `new_word_array`, which is returned as the ordered version of the input string.

Here is an example usage:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will return "Hello !!!Wdlor", which is the ordered version of the string where each word is replaced by a new word where all the characters are arranged in ascending order based on ASCII value, while keeping the order of words and blank spaces in the original string.