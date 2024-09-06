def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    
    # Extract substrings from the right half of the word.
    right_half = word[len(word) // 2 : ]
    right_half = right_half.lower()
    
    # Filter out vowels at the beginning or ending of the word.
    temp_list = [x for x in right_half if x not in vowel]
    
    if len(right_half) == 0:
        return ''
    
    # Find the index of the first consonant.
    first_consonant_idx = right_half.find(list(consonants)[0])
    
    if first_consonant_idx == -1:
        return right_half[0]
    
    # Find the closest vowel to the right of the first consonant.
    for i in range(first_consonant_idx + 1, len(right_half)):
        if right_half[i] in vowel:
            return right_half[i]
    
    return ''