```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using the `split()` method (considering spaces as separators), and then sorts the characters in each word individually and recursively. The sorted characters are then joined back together to form a new word, and these new words are concatenated together to maintain the original word order. This effectively completes the task of creating an ordered version of the input string, where each word is ordered based on the ASCII values of its characters.