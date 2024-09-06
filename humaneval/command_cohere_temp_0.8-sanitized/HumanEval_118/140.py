def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    
    # Extract substrings from the right, considering possible vowel placements
    right_consonant_chunks = [chunk for chunk in word.split('') if chunk not in vowel]
    right_vowels = [chunk for chunk in word.split('') if chunk in vowel]
    
    # Check if any right_vowels intersect with right_consonant_chunks
    for i in range(len(right_vowels)):
        if right_vows[i] in right_consonant_chunks:
            return right_vows[i]
    return ''