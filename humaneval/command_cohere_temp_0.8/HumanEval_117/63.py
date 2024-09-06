```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = [word for word in s.split() if word]
    return [word for word in words if count_consonants(word) == n]

# Test Cases
print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
```

This script splits the input string into words, and then iterates over each word to count the consonants, using a generator expression. It then filters the words based on the criteria of having exactly `n` consonants and returns them in the order they appear in the string. 

The output of the script is:
```
['little']
['Mary', 'lamb']
[]
['world']
['Uncle']
``` 

Which corresponds to the expected output for the test cases provided in the problem statement.