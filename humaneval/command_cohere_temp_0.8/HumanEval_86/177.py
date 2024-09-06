```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (assuming words are separated by spaces) and then sorts each word based on the ascii value of its characters, thus, arranging them in ascending order. The joined string is then returned to form the 'ordered version' of the input string as described in the problem statement. This algorithm's time complexity is `O(n log n)`, where n is the length of the input string, arising from the sorting step. The space complexity is `O(n)`, as it creates a new list of sorted words to not alter the original ones.