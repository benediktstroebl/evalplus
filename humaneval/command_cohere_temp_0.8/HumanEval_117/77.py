```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'y' and char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
           char != 'Y':
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
The provided Python script solves the problem by first creating a helper function **count_consonants(word)** that calculates the number of consonants in a given word. It checks each character of the word and increments a counter if the character is a consonant. 

Then, the main function **select_words(s, n)** splits the input string into a list of words and iterates through each word. It checks if the number of consonants in each word matches the desired count 'n', and if so, it adds the word to the **result** list. The final output is the list of words from the input string containing exactly 'n' consonants.

This solution allows for flexible and concise code, as the count_consonants() function can be reused for other tasks related to counting consonants, and the select_words() function can easily be adapted for other filtering tasks in future problems.