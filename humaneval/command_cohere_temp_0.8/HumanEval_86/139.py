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

The function `anti_shuffle` takes a string as input and returns a sorted version of the words within the string, keeping the word order intact. It achieves this by first splitting the input string into individual words using the `split()` method. It then iterates through each word, converting it into a character array and sorting it based on ASCII values. Finally, the sorted characters are concatenated back into a new word and added to the `new_word_array`, which is later joined together with spaces to form the final output string.

This approach ensures that the words in the input string are transformed to maintain the alphabetical order of their characters, while keeping the original word spacing and order intact.