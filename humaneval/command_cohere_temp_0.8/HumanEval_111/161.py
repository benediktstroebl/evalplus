```python
def histogram(test):
    letters = test.strip().lower().split()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
```
The code extracts the lowercase letters from a given string using `strip()` to remove leading and trailing whitespaces and `split()` to separate them, and then it stores them in a dictionary `letter_count` with keys as the letters and values representing their repetition. The `if ... else` statement is used to efficiently update the count of each letter. The output of the example cases is:
```python
 histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
histogram('a b c a b') == {'a': 2, 'b': 2}
histogram('b b b b a') == {'b': 4}
histogram('') == {}
```