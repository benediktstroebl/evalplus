```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    # Remove all vowels and consonants at the edge
    word = word.strip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if len(word) < 2:
        return ''

    # Find the closest vowel from the right side
    right_vowels = [c for c in word if c in vowels]
    if right_vowels:
        return min(right_vowels, key=lambda x: word.find(x))

    # If no right vowel, find from the left side
    left_vowels = [c for c in word if c in vowels]
    if left_vowels:
        return min(left_vowels, key=lambda x: word.rfind(x))

    return ''
```

This script assumes only letters from the English alphabet are present in the input word. It removes starting and ending vowels and consonants, then searches for the remaining vowels to find the closest vowel located between two consonants. If no such vowel is found, it checks from the left side of the word. If still nothing is found, an empty string is returned. 

This solution has a time complexity of `O(n)` where `n` is the length of the input `word`, and a space complexity of `O(1)`.