Here's a Python script that contains a function to solve the problem as asked:
```python
def count_consonants(word):
    count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and char != 'y':
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

The `count_consonants` helper function calculates the number of consonants in a given word, which is later used to filter the words with the desired consonant count. The `select_words` function splits the input string into a list of words, iterates through each word, and calculates the count of consonants for each word using the helper function. If the count matches the specified `n`, the word gets appended to the `result` list. Finally, the function returns the list of selected words.