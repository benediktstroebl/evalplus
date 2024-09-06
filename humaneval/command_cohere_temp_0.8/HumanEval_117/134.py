```python
def count_consonants(word):
    count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
           char != 'y' and char != 'Y':
            count += 1
    return count

def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```

The `count_consonants` helper function calculates the number of consonants in a given word, ensuring it counts only consonants occurring in the middle of the word (excluding vowels and y). The `select_words` function splits the input string into words and then iterates through each word, checking if its consonant count matches the desired `n`. If a word contains exactly `n` consonants, it's added to the result list, which is returned as the output. This approach enhances code readability and maintains a more understandable and concise solution for the given problem.