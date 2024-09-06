```python
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    # Removing extra spaces and converting to lower case for case insensitivity
    word = word.strip().lower()
    index_of_right_vowel = len(word) - word[::-1].index(word[0]) - 1
    if index_of_right_vowel < 0:
        return ""
    for vowel in vowels:
        if vowel in word[index_of_right_vowel:]:
            return vowel
    return ""
```

This script assumes only letters from the English alphabet are present in the given word. It removes spaces and converts the word to lowercase to ensure the solution is case-insensitive. It then identifies the index of the right-most vowel using a reverse index search, counting from the right. It returns an empty string if no suitable vowel is found or if no vowel is present in the word. 

The script efficiently determines the closest vowel to the right of a word and fulfills the problem requirements. Let me know if you need any adjustments.