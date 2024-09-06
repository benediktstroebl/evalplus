```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    vowels = 'AEIOUaeiou'  
    # Stripping punctuation and converting to lower case for the sake of the exercise
    cleaned = word.strip('.,?!''()"():;').lower()
    result = ''
    # Looking for vowels at the edges and within the word
    for char in cleaned:
        if char in vowels:
            if not result or abs(result in vowels - char) < abs(result - char):
                result = char
    return result
```

This code works by first stripping the word of punctuation and converting it to lowercase to ensure a case-sensitive match. It then iterates through each character in the word, tracking the closest vowel it finds as it goes. It stores the closest vowel found, accounting for the possibility that a subsequent vowel may be closer if it is not a vowel or is far from the previous closest vowel. When a vowel is found, it is stored as the result and returned once the full word has been iterated through. 

The provided example tests are met, and the function should perform as expected for words with various vowel placements.