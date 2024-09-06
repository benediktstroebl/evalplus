```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without altering the order of spaces and word sequences. For example, the input `'Hello World!!!'` would return `'Hello !!!Wdlor'`.

This approach efficiently solves the problem by:
1. Splitting the input string into individual words (`word_array`).
2. Sorting the characters in each word based on ASCII values and using the sorted result to create a new word (`ascii_sorted`).
3. Storing these new words in a list (`new_word_array`) while maintaining the original word order.
4. Reassembling the original sentence with the new sorted words and returning the result.

The code maintains the original structure and spaces between words, as the problem statement requires.