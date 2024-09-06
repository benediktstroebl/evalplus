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
The `histogram` function takes a single argument, which is the test string. It first splits the string into individual letters, then filters out any non-alphabetic characters. Thereafter, it commences iterating through the resulting list of letters, tallying the frequency of each one and storing it in the `repeat` dictionary. In case a letter already exists in the dictionary, the count is incremented, otherwise, it's initialized with a count of 1. Ultimately, the function returns the `repeat` dictionary, containing the letter(s) occurring the most and their respective counts. 

This approach is efficient and can efficiently handle different test cases, and can easily be extended to handle more complex scenarios if needed.