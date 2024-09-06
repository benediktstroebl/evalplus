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
The function creates a dictionary, `letter_count`, that will be used to count the letters in the given string. In an iterative approach, it iterates through each letter, converts them to lowercase to ensure consistency, and assigns them to the dictionary. The count of the letters is incremented by one and if a letter is not in the dictionary, it is added with a count of one. Finally, the dictionary returns the final count of each letter. 

This approach is simple and straightforward, and it should work correctly for the given problem statement.