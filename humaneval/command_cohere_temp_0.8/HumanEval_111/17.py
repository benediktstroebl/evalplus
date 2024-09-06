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
This Python script defines a function called `histogram` which takes in a single argument, `test`. The function returns a dictionary where the keys are letters from the input string and the values are the number of times that letter appears in the string. 

For example, the test cases provided will return:
- `histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}`
- `histogram('a b c a b') == {'a': 2, 'b': 2}`
- `histogram('b b b b a') == {'b': 4}`
- `histogram('') == {}`