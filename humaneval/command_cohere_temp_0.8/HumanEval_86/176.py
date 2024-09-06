```python
def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s) if char != " " and char != ""]
    sorted_words = [chr(int(c)) for char in s for c in sorted(char)]
    return " ".join(sorted_words)[word_inds]
```

The function uses a list comprehension to find the indices of all words (where the character is not a space or an empty string). Then, it creates a list of all characters sorted by ASCII value. Finally, it uses these indices to slice the sorted character list and reconstructs the original words. The result is a string where all words are sorted by ASCII value, while keeping the original order of words and spaces. 

Such solutions result from the **greedy** algorithm, which tends to work well with **ASCII** values. It helps to sort all the words, without considering any word complexities like **case**, **punctuation**, **numbers**, and so on. Thus, maximizing the **locale-independent** nature of **ASCII**.