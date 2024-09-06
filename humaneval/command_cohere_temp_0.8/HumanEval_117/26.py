```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char.isalpha():
            if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                cnt += 1
    return cnt

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script solves the problem by first creating a helper function `count_consonants` that takes a word as input and returns the number of consonants in the word. This is achieved by iterating over each character in the word and checking if each character is an alphabetic character; if so, it checks if the character is a consonant, incrementing a counter if it is. 

The `select_words` function takes the input string `s` and the target number of consonants `n`. It first splits the input string into a list of words, then iterates through each word, checking if the number of consonants matches the target with each word being added to the result list if it does. 

The script successfully passes the tests outlined in the problem statement:
```python
>>> select_words("Mary had a little lamb", 4)
['little']

>>> select_words("Mary had a little lamb", 3)
['Mary', 'lamb']

>>> select_words("simple white space", 2)
[]

>>> select_words("Hello world", 4)
['world']

>>> select_words("Uncle sam", 3)
['Uncle']
```