```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char.isalpha():
            if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u':
                cnt += 1
    return cnt

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script solves the problem by first creating a helper function `count_consonants(word)` that calculates the number of consonants in a given word. The function uses a for loop to iterate over each character in the word, if the character is an alphabet letter, it checks if the lowercase version of the character is not a vowel (excluding 'y'), and if so, it increments a counter. 

The `select_words(s, n)` function takes the input string `s` and the target number of consonants `n`. It first splits the input string into a list of words using the `split()` method (assuming the input string contains only letters, spaces, and/or punctuation). Then, it iterates over each word in the list of words, checks the count of consonants using the `count_consonants()` helper function, and if the count matches the target, appends the word to the `result` list. 

The final list of words with n consonants is returned.