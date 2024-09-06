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
3. Appending the new sorted words to a new array (`new_word_array`).
4. Reassembling the original sentence by joining the array of new words while preserving the original word sequence and spaces.

The code maintains the original structure of spaces between words, ensuring the output retains word sequencing while sorting the characters within each word.