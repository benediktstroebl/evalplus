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

The solution works by first converting the input string into lowercase and then iterating over each letter. For each letter, it increments the count if the letter is already in the dictionary, or initializes the letter with a count of 1 if not. Finally, it returns the dictionary with the counts for each letter. 

This approach is O(n) where n is the length of the input string, as it requires converting the string to lowercase and iterating through each character exactly once to populate the dictionary. It also has a dictionary lookup for each letter, which is typically O(1). Overall, it's an efficient solution with a time complexity of O(n). 

This problem can also be solved using a Counter from the collections module, with a slightly more concise implementation:
```python
from collections import Counter

def histogram(test):
    return Counter(test.lower())
```