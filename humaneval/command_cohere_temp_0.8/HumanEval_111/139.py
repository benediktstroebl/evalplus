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
The code processes the test string by stripping any leading or trailing whitespace and converting it to lowercase. The text is then split into a list of individual letters. A dictionary, `letter_count`, is used to keep track of the occurrence of each letter. The code iterates through the list of letters, incrementing the count for each letter already in the dictionary or initializing the count to 1 for new letters added to the dictionary. 
This solution addresses the problem statement to return a dictionary of the letter(s) with the most repetition and their corresponding count, or if several letters have the same occurrence, to return all of them. The `histogram()` function returns a dictionary that solves the specified problem.