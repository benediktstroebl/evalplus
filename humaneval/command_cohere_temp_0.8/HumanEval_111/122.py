```python
def histogram(test):
    letters = test.split()
    letters = [letter for letter in letters if letter.isalpha()]
    repeat = {}
    for letter in letters:
        if letter in repeat:
            repeat[letter] += 1
        else:
            repeat[letter] = 1
    return repeat
```
The function splits the input test string and filters out non-alphabetic characters. It then iterates over the alphabetic characters, keeping a dictionary of their occurrence(s). If the letter is already in the dictionary, the count is incremented; otherwise, it's added with a count of 1. This approach ensures accuracy for the given problem and aligns with the specified expected outputs.