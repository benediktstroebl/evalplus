```python
def histogram(test):
    letters = test.strip().lower().split()
    count = {}
    for letter in letters:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count
```
The function creates a dictionary where the keys are the letters and the values are the counts. It uses a for loop to iterate through each letter in the string, and if the letter is already in the count dictionary, the count is incremented; otherwise, the letter is added to the dictionary with a count of 1. This approach ensures that the dictionary reflects the letter counts accurately, and it returns the dictionary as the solution.