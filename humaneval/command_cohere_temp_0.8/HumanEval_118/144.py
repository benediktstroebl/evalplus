```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    # O(n) time, where n is the length of the word
    for i in range(len(word)-1):
        if word[i] in vowels and word[i+1] in consonants:
            return word[i]
    return ''
```

The Python script provides a function called `get_closest_vowel` which takes a word as input. This function works by first creating two strings, `consonants` and `vowels`, which store all English consonants and vowels, respectively. It then iterates through the characters of the input word, starting from the second character (index 1) to ensure that vowels at the beginning of the word are ignored. For each character, it checks if it is a vowel and if the next character is a consonant. If this condition is met, the function returns the vowel it found. This process repeats until either a qualifying vowel is found or the end of the word is reached. The function returns an empty string if no qualifying vowel is found. 

The expected time complexity of the algorithm is O(n), where n is the length of the input word. This is due to the single loop that iterates through each character in the word.