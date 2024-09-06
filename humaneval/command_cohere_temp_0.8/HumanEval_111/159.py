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

The `histogram()` function takes a string as input and returns a dictionary of the letters in the string with the most repetition and their corresponding counts. If several letters have the same occurrence, it returns all of them. 

This solution works by using a dictionary to keep track of the counts of each letter. The code first converts the input string to lowercase to ensure consistency in counting. It then iterates through each letter in the string, and for each letter, it increments its count in the dictionary. If the letter is not already in the dictionary, it is added with a count of 1. After processing all the letters, the dictionary contains the required information, which is then returned. 

This solution is concise and efficient in solving the problem.