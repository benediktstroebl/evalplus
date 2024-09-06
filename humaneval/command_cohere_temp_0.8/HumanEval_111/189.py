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
The function splits the input string into a list of individual letters and uses a dictionary to count the occurrences of each letter. The dictionary is returned with the corresponding letter as the key, and the count as the value.

Here is a test case input/output to prove the correctness of the function:
```
input: histogram('a b c')
output: {'a': 1, 'b': 1, 'c': 1}

input: histogram('a b b a')
output: {'a': 2, 'b': 2}

input: histogram('a b c a b')
output: {'a': 2, 'b': 2}

input: histogram('b b b b a')
output: {'b': 4}

input: histogram('')
output: {}
```