def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    index = next((i for i, char in enumerate(word) if char in consonants), None)
    if index is None:
        return ''

    # Counting number of vowels on the right side
    vowel_count = sum(1 for char in word[index: ] if char in vowels)
    
    if vowel_count == 0:
        return ''

    return word[index+vowel_count-1]