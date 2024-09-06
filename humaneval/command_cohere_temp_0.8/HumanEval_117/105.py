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
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script solves the problem by first creating a helper function `count_consonants` that takes a word as input and calculates the number of consonants present in that word. The function `select_words` splits the input string into a list of words, then iterates through each word, calculates its consonant count using the helper function, and appends it to the `result` list if the consonant count matches the desired count `n`. The script returns the `result` list containing the selected words. 

This solution adheres to the problem statement by considering only letters, spaces, and the specified count of consonants. The code is concise and efficiently handles the tasks of counting consonants and selecting words based on the consonant count. It handles all the edge cases mentioned in the problem statement, including empty input and words with varying numbers of consonants.