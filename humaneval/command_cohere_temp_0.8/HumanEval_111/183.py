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
The `histogram()` function takes a string as input and returns a dictionary of the letters in the string and their corresponding counts. 
It uses a for loop to iterate through each letter in the string, and increments the count for each letter in the `letter_count` dictionary. 

This approach assumes that the input will only contain lowercase letters, so it converts the input to lowercase using the `lower()` method, and handles the case where the input is an empty string. 

The example usage demonstrates the function's expected behavior for different test cases.