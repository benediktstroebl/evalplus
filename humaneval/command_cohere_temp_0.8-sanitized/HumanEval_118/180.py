def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    # Convert the word to lowercase to make the comparison case insensitive
    word = word.lower()
    
    # Split the word into individual characters and initialize the previous consonant and current vowel variables
    word = list(word)
    prev_consonant = True
    current_vowel = ''
    
    for char in word:
        if char in vowels:
            if not prev_consonant:
                current_vowel = char
        elif char in consonants:
            prev_consonant = True
        else:
            # If the character is not a consonant or a vowel, it is not taken into account for the closest vowel computation
            continue
    
    # If the above loop completes without setting a valid current_vowel, return an empty string
    if not current_vowel:
        return ''
    
    # If the end of the word is reached and there is no consonant after the current vowel, it is the closest vowel
    if not prev_consonant:
        return current_vowel
    
    # If the above conditions are not met, the closest vowel is the first vowel encountered after the last consonant
    return current_vowel