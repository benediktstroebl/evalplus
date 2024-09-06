```python
def count_consonants(word):
    count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            count += 1
    return count

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, while the `select_words` function splits the input string into a list of words and then iterates through each word, checking if its consonant count matches the required count `n`, if so, it adds the word to the `result` list. 

Here is an example usage of the function for the first test case:
```python
select_words("Mary had a little lamb", 4)
```
The output will be:
```
['little']
```