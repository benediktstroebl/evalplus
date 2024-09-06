```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using the `split()` method (considering spaces as the delimiter), and then sorts the characters in each word based on their ASCII values. The sorted words are then reassembled into a new string, maintaining the original spacing between words. The function's result would be the ordered version of the input string, where each word contains characters sorted in ascending order.