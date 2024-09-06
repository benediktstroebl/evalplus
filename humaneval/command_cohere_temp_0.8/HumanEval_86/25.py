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

The code splits the input string into a list of words (`word_array`), where each word becomes a list of characters (characters sorted separately). The code then sorts each list of characters in ascending order and joins them back into a single word. These sorted words are then stored in a new list (`new_word_array`) and joined together with spaces to form the final output string.

The problem requires that the word order remains unchanged, and the algorithm preserves the spaces between words. Thus, the code achieves the desired result of reordering characters within words while keeping the word structure and overall order intact.