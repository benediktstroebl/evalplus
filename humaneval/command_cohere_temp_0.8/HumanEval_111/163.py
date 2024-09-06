```python
def histogram(test):
    letters = test.split()
    letters = [letter for letter in letters if letter.isalpha()]
    counter = {}
    for letter in letters:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter
```
The function uses a few Python concepts including splitting strings, filtering out non-alphabetic characters, and using a dictionary to store the letter counts. Different test cases are provided to test the function and ensure it outputs the expected results.