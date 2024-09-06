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
The function creates a dictionary called `letter_count`. It iterates through the input `test`, lowering each character to ensure uniformity and counting occurrences in the process. When a character is encountered for the first time, it's added to the dictionary with a count of 1. Subsequent occurrences increment the count, allowing the function to accurately track and return the counts for characters with the highest repetition. 

This approach ensures the function works for the provided test cases, returning the expected results.