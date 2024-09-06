```python
def count_consonants(word):
    count = 0
    for char in word:
        if char.isalpha():
            if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                count += 1
        elif char == ' ':
            continue
        else:
            return 0
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
The `count_consonants` helper function calculates the number of consonants in a given word, ignoring spaces. The main `select_words` function splits the input string into a list of words, iterates through each word, and checks if its consonant count matches the desired count `n`. If a word has exactly `n` consonants, it's added to the `result` list, which is then returned. 

This solution adheres to the problem statement by considering only letters and spaces, and it provides the required words in the order they appear in the string.