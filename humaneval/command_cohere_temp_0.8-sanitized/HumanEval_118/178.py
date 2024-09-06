def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    
    # Find the first vowel that is preceded and followed by consonants
    closest_vowel = next((c for c in word if c in vowel and
                        (word[0] in consonants or c == word[0]) and
                        (word[-1] in consonants or c == word[-1])),
                      None)
    
    return closest_vowel