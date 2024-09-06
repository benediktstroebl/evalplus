```python
def count_consonants(word):
    cs = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            cs += 1
    return cs

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script solves the problem by first creating a new function called `count_consonants(word)` that takes a word as input and returns the number of consonants present in that word. It uses a loop to iterate through each character in the word, and if the character is a consonant (or vowel), it increments a counter. 

Then, the main function `select_words(s, n)` splits the input string into a list of words and iterates through each word. For each word, it checks if the count of consonants matches the desired count `n`, and if so, it adds the word to the `result` list. Finally, the function returns the `result` list, which contains all the words that contain exactly `n` consonants.

This solution is efficient since it linearly traverses the input string, and the consonant-counting process for each word is also linear. Thus, the time complexity of the solution is O(m), where `m` is the length of the input string. Additionally, the space complexity is O(1) since the additional space used is limited to storing a single list, which is the result list `result`.