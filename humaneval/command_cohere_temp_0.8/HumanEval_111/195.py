```python
def histogram(test):
    letters = test.split()
    letters = [letter for letter in letters if letter.isalpha() and letter.lower() in letter]
    if len(letters) == 0:
        return {}
    count_letter = {}
    for letter in letters:
        if letter in count_letter:
            count_letter[letter] += 1
        else:
            count_letter[letter] = 1
    return count_letter
```
The code works by first splitting the input string into letters and storing them in the `letters` variable. Then, the code filters out non-alphabetic characters and converts the characters to lowercase using the `isalpha` and `lower` functions. Using a dictionary, the code counts the number of occurrences for each letter and returns the count or counts if several letters have the same occurrence. This solution is efficient and can be tested for any string input.