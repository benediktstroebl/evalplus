```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []

    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)

    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (using split()) and then sorts each word based on ASCII values and finally joins all the sorted words to get the desired output. It ensures the exact character ordering requirement specified in the prompt.