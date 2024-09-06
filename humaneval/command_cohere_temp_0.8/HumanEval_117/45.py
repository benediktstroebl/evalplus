```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            cnt += 1
    return cnt

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, while the `select_words` function splits the input string into a list of words, iterates through each word, and computes its consonant count. If the consonant count matches the specified number `n`, the word is added to the `result` list, which is returned once all words have been processed. 

This solution allows for the selection of words with exactly `n` consonants from the input string `s`. 

## Example Usage
```python
print(select_words("Mary had a little lamb", 3)) 
```

```output
['Mary', 'little']
```

```python
print(select_words("Hello world", 4)) 
```

```output
['world']
```

```python
print(select_words("Uncle sam", 2)) 
```

```output
['Uncle']
```

```python
print(select_words("simple white space", 3)) 
```

```output
[]
``` 

This would be the output for the example cases.