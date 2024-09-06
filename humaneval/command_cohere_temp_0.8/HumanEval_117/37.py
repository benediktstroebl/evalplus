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
The provided Python script solves the problem by first creating a helper function `count_consonants(word)` that calculates the number of consonants in a given word. The function uses a for loop to iterate over each character in the word, if the character is an alphabet character, the function checks if the character is a vowel, if it is not, then it increments the consonant count. 

The `select_words(s, n)` function takes the input string `s` and integer `n` as arguments. It first splits the input string into a list of words using the `split()` method (note: this assumes the input string contains only letters, spaces, and/or punctuation, and each word is separated by one or more spaces). Then, it iterates over each word in the list of words, calculates the number of consonants in each word using the `count_consonants()` function, and checks if this count matches the given criteria. If a word contains exactly `n` consonants, it is added to the `result` list. 

Finally, the function returns the `result` list of words that contain exactly `n` consonants. This approach ensures that the list is inclusive of words that meet the criteria, and the order is maintained from the original string. 

Overall, the code timescope is O(n + m), where n is the number of words and m is the maximum number of consonants in a word. The `count_consonants()` function iterates over each word once, and the `select_words()` function iterates over each word list once.