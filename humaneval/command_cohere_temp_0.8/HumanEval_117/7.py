```python
def count_consonants(word):
    """
    Counts the number of consonants in a word
    """
    word = word.lower()
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total

def select_words(s, n):
    """
    Returns a list of words from string s that contain exactly n consonants
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```

Here is an example of how to use the above function to solve the problem statement:
```python
answer = select_words("Mary had a little lamb", 3)
print(answer)  # Output: ['Mary', 'lamb']
``` 

This script assumes that the input string contains only letters and spaces, and that each word contains at least one consonant (otherwise the word would not be included in the result). It also converts each word to lowercase before counting consonants, to make the counting logic simpler. 

This solution could potentially fail for edge cases like an all-consonant input string (e.g., 'allconsonants'), or cases where the input string contains uppercase letters, but these conditions are not explicitly mentioned in the problem statement, and thus would likely be considered out of scope.