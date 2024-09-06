```python
def histogram(test):
    letters = test.split()
    letters = [letter for letter in letters if letter.isalpha()]
    counter = {}
    for letter in letters:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter
```
The `histogram` function first splits the input test string into letters and removes any non-alphabetic characters. It then iterates through each letter and keeps a tally in the counter dictionary, incrementing the count for each letter as it appears in the string. Finally, the dictionary containing the letter and its corresponding count is returned. 

This approach is concise, efficiently solves the problem, and should help you pass any unit tests. Let me know if you'd like me to help with any additional problems or clarify other concepts!