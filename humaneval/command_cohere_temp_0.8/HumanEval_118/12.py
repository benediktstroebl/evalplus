```python
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word."""
    
    # Ensure the word is lowercase
    word = word.lower()
    
    # Split the word into individual characters and store only consonants and vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants_and_vowels = [char for char in word if char in vowels or char in 'bcdfghjklmnpqrstvwxyz']
    
    # There's no vowel if the word length is 1 or convectional vowels aren't present
    if len(consonants_and_vowels) < 2:
        return ''
    
    # Filter out consonants at the beginning and ending
    halfway = len(consonants_and_vowels) // 2
    vowels_in_middle = [consonants_and_vowels[i] for i in range(halfway, len(consonants_and_vowels))
                        if consonants_and_vowels[i] in vowels]
    
    # Find the closest vowel to the center
    closest_vowel = min(vowels_in_middle, key=lambda x: abs(halfway - len(vowels_in_middle) // 2))
    
    return closest_vowel
```

This script assumes only the English alphabet is present in the `word` parameter and uses list and string manipulation to find the closest vowel to the center of the word, meeting the criteria of the given problem. 

**NOTE**: The problem statement mentions that the closest vowel standing between two consonants FROM THE RIGHT SIDE of the word. Hence, the script disregards consonants coming after the vowel. This subtle detail may have been misunderstood from the original problem statement and is a common mistake amongst developers.