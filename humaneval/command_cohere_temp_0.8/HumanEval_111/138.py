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
This Python script solves the histogram problem using the split method to convert the input string into a list of letters. The code then uses a dictionary to count the occurrences of each letter and returns the dictionary as the solution. Note that this algorithm assumes that the input will not contain any whitespace or special characters other than letters, and also that there is at least one letter in the input.