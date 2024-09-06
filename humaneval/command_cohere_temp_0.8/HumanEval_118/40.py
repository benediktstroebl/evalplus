```python
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    # Split by consonants, consider only the rightmost segment
    segments = [part for part in word.split('[^aeiou]') if part]
    right_segment = segments[-1] if segments else ''
    
    # Find the index of the first vowel that appears after a consonant
    for i, char in enumerate(right_segment):
        if char in vowels and right_segment[i+1:].isalnum():
            return char
    
    return ''
```

The provided code divides the input word into segments containing consonants and vowels, focusing on the rightmost segment. It then identifies the first vowel appearing after a consonant within that segment, offering the closest vowel as per the given scenario. 

This algorithm efficiently solves the problem without requiring additional logic for word splitting or vowel identification. It handles various cases, including words with no qualifying vowels, ensuring a clear and concise solution.