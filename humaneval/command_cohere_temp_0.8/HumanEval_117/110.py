```python
def count_consonants(word):
    consonants = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants += 1
    return consonants

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script solves the problem by first defining a function `count_consonants` that calculates the number of consonants in a given word. It iterates through each character in the word and counts the characters that qualify as consonants. 

Following that, the main function `select_words` splits the input string into a list of words and then iterates through each word. It checks if the count of consonants in each word matches the desired number `n`, and if so, it adds the word to the `result` list. The final output is the list of words from the input string containing exactly `n` consonants, in the order they appear in the string. 

This solution addresses the given challenge, and the function `select_words` is capable of handling different scenarios and test cases as specified in the problem statement.