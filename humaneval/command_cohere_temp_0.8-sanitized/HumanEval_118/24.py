def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    # Remove the first and last character if it's a vowel
    if word[0] in vowels:
        word = word[1:]
    if word[-1] in vowels:
        word = word[:-1]
    
    # Iterate from the right side of the word
    for i in range(len(word)-2, -1, -1):
        if word[i] in consonants and word[i+1] in consonants:
            if i > 0 and word[i-1] in vowels:
                return word[i-1]
            if i < len(word)-1 and word[i+1] in vowels:
                return word[i+1]
    
    return ""