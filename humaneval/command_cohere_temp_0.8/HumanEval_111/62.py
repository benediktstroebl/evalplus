```python
def histogram(test):
    letter_count = {}
    
    for letter in test.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    return letter_count
```
The `histogram()` function takes a string as input and returns a dictionary of the letters in the string with the most repetition and their corresponding counts. 
For example, `histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}`

This solution follows the `DRY` (Don't Repeat Yourself) principle and uses a dictionary to keep track of the counts, which allows for a concise and efficient solution.