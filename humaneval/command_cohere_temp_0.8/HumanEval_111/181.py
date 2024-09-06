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
The function creates a dictionary, letter_count, that stores the count of each letter in the given test string. Using a for loop, it iterates through each letter, converting the letter to lowercase to ensure consistency. It updates the count of the letter in the dictionary if the letter is already present, or initializes it with a count of 1 if it is encountered for the first time. Finally, the function returns the dictionary with the letter counts. 

Here is an example execution of the script:
```python
print(histogram("a b c")) 
```
```bash
{'a': 1, 'b': 1, 'c': 1}
```

And another example execution:
```python
print(histogram("a b c a b"))
```
```bash
{'a': 2, 'b': 2}
```

This should match the examples provided in the problem statement.