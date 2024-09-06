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
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```

The `count_consonants` helper function calculates the number of consonants in a given word. It iterates through each character in the word and checks if the character is a consonant. The select_words function splits the input string into a list of words, iterates through each word, and checks if the number of consonants in each word is equal to the target number `n`. If so, the word is added to the result list.

The code assumes that the input string contains only letters and spaces, which is the stated assumption for the given problem.

The function returns an empty list if the input string is empty.

The provided examples in the prompt match the expected behavior of the code.