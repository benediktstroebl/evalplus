def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    # Remove all vowels and consonants at the edge
    word = word.strip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if len(word) < 2:
        return ''

    # Find the closest vowel from the right side
    right_vowels = [c for c in word if c in vowels]
    if right_vowels:
        return min(right_vowels, key=lambda x: word.find(x))

    # If no right vowel, find from the left side
    left_vowels = [c for c in word if c in vowels]
    if left_vowels:
        return min(left_vowels, key=lambda x: word.rfind(x))

    return ''