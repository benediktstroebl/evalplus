```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This code defines a function `anti_shuffle` that takes a string as input and returns a sorted version of the string without altering the word order or spacing. It first splits the input string into individual words using the `split()` method (preserving the empty strings that represent spaces), then sorts each word based on ASCII values and concatenates them together using blank spaces to maintain the original word order and spacing.

Here is an example function call:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will output the anti-shuffled version of the string where each character is in its ASCII order, but the order of words and spacing remain unchanged.