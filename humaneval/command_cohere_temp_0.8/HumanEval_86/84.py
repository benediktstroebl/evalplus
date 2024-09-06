```python
def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s) if char != " " and char != ""]
    sorted_words = [chr(int(c)) for char in s for c in sorted(char)]
    return " ".join(sorted_words[i] if i in word_inds else " " for i in range(len(sorted_words)))
```

The provided Python script defines a function `anti_shuffle` that takes a string as input and returns an ordered version of the string as described in the prompt.

This function works by first identifying the indices of all non-blank, non-space characters in the string. Then, it sorts these characters based on their ASCII values and reconstructs the words using these sorted characters while preserving the original word boundaries and spaces. The resulting string is returned.