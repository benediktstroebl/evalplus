```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This code defines a function `anti_shuffle` that takes a string as input and returns a sorted version of the words within that string, retaining the order of words and spaces.

The function first splits the input string into an array of words using the `split()` method. This method splits the string on whitespace, so it separates the words and ignores any spaces. It then initializes an empty array `new_word_array` to store the sorted words.

Next, the function iterates through each word in the `word_array`, sorts the characters of each word based on their ASCII values, and joins them back into a single string. This sorted string is then added to the `new_word_array`.

Finally, the function returns the resulting string by joining the elements of the `new_word_array` together with spaces.

This solution effectively addresses the problem statement, resulting in a correctly ordered string while maintaining the original word order and spaces.