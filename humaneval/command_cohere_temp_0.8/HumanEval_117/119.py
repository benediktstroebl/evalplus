```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total

def select_words(s, n):
    """Return list of words with exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        cnt = count_consonants(word)
        if cnt == n:
            result.append(word)
    return result
```
The `count_consonants` identifies each letter as a consonant or not, it contributes its count to a running total. The given `select_words` function processes each word in the string and checks if its consonant count matches the required number, if so, it adds it to the result list. 
The expected output is achieved by considering both the occurrence of the word and the count of consonants within each word. This is showcased in the example:
```python
select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
``` 
The output is achieved by considering both the occurrence of the word and the count of consonants within each word. This is correctly illustrated in the example above.