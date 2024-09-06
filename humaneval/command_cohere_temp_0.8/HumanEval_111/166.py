```python
def histogram(test):
    letters = test.lower().strip().split()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
```
The `histogram()` function takes a string as input and returns a dictionary of the letters in the string and their corresponding counts. 

To solve the problem, the following steps are followed:
1. The input string is converted to lowercase using the `lower()` method and any leading and trailing white spaces are removed using the `strip()` method.
2. The string is then split into a list of individual letters using the `split()` method, with each letter being a string in the list.
3. A dictionary `letter_count` is initialized to store the counts of each letter.
4. A loop is used to iterate over each letter in the list of letters obtained from the split step.
5. For each letter, the code checks if the letter already exists in the `letter_count` dictionary using the `letter in letter_count` condition. This check is to avoid adding a letter more than once.
6. If the letter exists, the count of the letter is incremented by 1 using the `+= 1` operation. Otherwise, a new entry is created in the `letter_count` dictionary with the letter as the key and the count as the value.
7. The `letter_count` dictionary is returned as the final result.

This problem can also be solved using Python's ` Counter` class, here's a version of the code using that approach:
```python
from collections import Counter

def histogram(test):
    return dict(Counter(test.lower().strip()))
```
Here, the `Counter` class is used to count the occurrences of letters in the string, and the result is converted into a dictionary. As shown, multiple approaches can be used to solve a particular problem, choosing the one that suits you best is beneficial.