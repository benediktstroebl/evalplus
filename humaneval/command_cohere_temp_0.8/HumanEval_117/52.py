```python
def count_consonants(word):
    counts = 0
    for char in word:
        if char.isalpha():
            if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u':
                counts += 1
    return counts

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` helps determine the count of consonants for a given word whereas the `select_words` function goes through each word in the string and checks if the count of consonants matches the desired count 'n'. Using the split method, it iterates over words separated by spaces, and for each word, it counts the consonants using the helper function, if the count matches, the word is added to the result list that is returned at the end. 

This solution assumes that the complexity of splitting a string into words is negligible compared to the complexity of counting consonants in a word, so the additional overhead of splitting the string into words at each step is offset by the reduced complexity of counting consonants. 
```python
word = "mess"
print(count_consonants(word))
```
The output for this example is `3`, which demonstrates the functioning of the `count_consonants` function. 

```python
select_words("Mary had a little lamb", 3)
```
The output for this example is `["Mary", "lamb"]`, which demonstrates the functioning of the `select_words` function.