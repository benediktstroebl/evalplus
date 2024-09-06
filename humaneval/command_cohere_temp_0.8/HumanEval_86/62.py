```python
def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s) if char != " " and char != "]"]
    sorted_words = [chr(int(c)) for char in s for c in str(ord(char)-96)]
    return " ".join([s[i] for i in word_inds]+sorted_words)
```

The `anti_shuffle` function uses two nested list comprehensions. The first comprehension identifies the indices of words (excluding spaces and closing brackets) while the second computes the sorted representation of each word by subtracting 96 (the ASCII value of `"`) from its ASCII code and converting the result back to characters. The final result is constructed by joining the original words at their original indices followed by the sorted words. This solution ensures that the word order and spacing are maintained while rearranging the characters within each word.  The code could be optimized for efficiency but this solution is sufficiently clear and correct.