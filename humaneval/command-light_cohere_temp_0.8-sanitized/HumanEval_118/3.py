def get_closest_vowel(word):
    vowels = {"a", "e", "i", "o", "u"}
    
    # Get all consonants in the word
    consonants = [c for c in word if c.isalpha()]
    
    # Index of the closest vowel is the one that is less than the total length of the word.
    closest_vowel = ""
    for vowel in vowels:
        if word[len(word) - 1 - index] == vowel:
            closest_vowel = vowel
            break
    return closest_vowel