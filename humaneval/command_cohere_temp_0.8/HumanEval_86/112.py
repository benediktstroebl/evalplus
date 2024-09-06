```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without altering the word order and spacing. It splits the input string into words using whitespace as the delimiter. For each word, it sorts its characters based on their ASCII values and joins them back to form a new word. These new sorted words are then appended to a new array, and the final sorted version of the input string is created by joining these new words with spaces.

Here's an example usage:
```python
print(anti_shuffle("Hello World!!!")) # Output: "Hello !!!Wdlor"
```

This will output: "Hello !!!Wdlor", where the characters of each word are sorted alphabetically, but the words and spaces remain in their original order.