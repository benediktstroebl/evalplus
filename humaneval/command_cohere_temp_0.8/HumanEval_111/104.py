```python
def histogram(test):
    letters = test.split()
    count = {}
    for letter in letters:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count
```
The function creates an empty dictionary count, then iterates through each letter in the test string, incrementing the count of each letter by 1. If the letter is not already in the count dictionary, it is added with a count of 1.

This algorithm is both efficient in time and space, as it takes linear time to iterate through the input string and constant space to maintain the dictionary, regardless of the input size. 

 Required output for the provided examples is:
```
{'a': 2, 'b': 2}
{'b': 4, 'a': 2}
{'a': 1, 'b': 1, 'c': 1}
{'b': 4}
{}
```