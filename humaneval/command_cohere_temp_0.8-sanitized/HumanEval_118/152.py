def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    
    # Extract substrings from the right half that ends with a consonant
    right_half = [end for end in word[1:].split('', 1) if end.lower() in consonants]
    
    # Check if the right half has a vowel standing between two consonants
    if right_half and right_half[0][-1] in vowel and right_half[1].lower() in vowel:
        return right_half[0][-1]
    elif right_half and right_half[-1].lower() in vowel:
        return right_half[-1]
    else:
        return ''