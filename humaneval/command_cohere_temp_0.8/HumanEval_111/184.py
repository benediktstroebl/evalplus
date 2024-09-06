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
The function creates a dictionary called `letter_count`, where the keys are lowercase letters, and the values are the number of times that letter appears in `test`. It iterates through every character in `test`, and if the character is already in `letter_count`, it increments its count. If not, it adds the character to `letter_count` with a count of 1. It then returns `letter_count`. 

This approach results in a straightforward solution that is both concise and efficient. It is less efficient compared to other solutions but remains effective for most uses, as the worst-case scenario would require looking up, inserting, or updating operations in a dictionary, which has an O(1) average time complexity.