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

Let's break down the solution into steps along with explanations:
1. `letter_count = {}`: Initializes an empty dictionary to store letters as keys and their counts as values. Using a dictionary ensures efficient retrieval of letters with the highest counts.
2. `for letter in test.lower()`: Iterates through each letter in the input string, converting it to lowercase to ensure consistency, and compatibility with the stated requirement of checking for lowercase letters only.
3. `if letter in letter_count`: Checks if the current letter is already a key in the `letter_count` dictionary. If it is, this indicates that the letter has appeared previously in the string, so its count needs to be incremented.
4. `letter_count[letter] += 1`: If the letter is already in the dictionary, this operation increments its count. If the letter is not found, it's added to the dictionary with a count of 1.
5. `return letter_count`: After processing all letters, the function returns the resulting dictionary containing the letter counts.

This solution leverages Python's dictionary data structure and its efficient operations to achieve the goal in a concise and efficient manner. While the problem could potentially be solved in one line using Python's built-in collections module, it's important to understand the underlying logic and the reason behind the choice of data structure. Using a dictionary to solve this problem exemplifies its efficiency in storing and retrieving data based on keys, which is a fundamental concept in data structures and algorithms.