```python
def count_consonants(word):
    return sum(1 for char in word if char.isalnum() and char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u')

def select_words(s, n):
    words = [word for word in s.split() if word]
    return [word for word in words if count_consonants(word) == n]
```
The `count_consonants` helper function calculates the number of consonants in a given word, excluding vowels (`a`, `e`, `i`, `o`, `u`). The function uses an iterative sum to count the alphanumeric characters, considering them as consonants if they are not any of the mentioned vowels.

The `select_words` function splits the input string into a list of words, then filters this list to include only words with a specified count of consonants using a list comprehension and the `count_consonants` helper.

The code assumes the input string contains only letters and spaces, and the output list is returned in the order these words appear in the string. These assumptions align with the problem statement provided.

This solution works by directly implementing the defined logic for counting consonants and selecting words, which is straightforward and effective. However, it could be optimized from a computational perspective. The vowel exclusions in the `count_consonants` function could be slower in terms of computation with long strings or large lists of words, as it iterates through each character in the word regardless of whether it is a vowel or not. Nevertheless, given the relatively simple nature of the problem, this is still an optimally efficient solution.