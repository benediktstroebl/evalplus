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