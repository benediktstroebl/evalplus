def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word."""
    
    # Ensure the word is lowercase
    word = word.lower()
    
    # Split the word into individual characters and store only consonants and vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants_and_vowels = [char for char in word if char in vowels or char in 'bcdfghjklmnpqrstvwxyz']
    
    # There's no vowel if the word length is 1 or convectional vowels aren't present
    if len(consonants_and_vowels) < 2:
        return ''
    
    # Filter out consonants at the beginning and ending
    halfway = len(consonants_and_vowels) // 2
    vowels_in_middle = [consonants_and_vowels[i] for i in range(halfway, len(consonants_and_vowels))
                        if consonants_and_vowels[i] in vowels]
    
    # Find the closest vowel to the center
    closest_vowel = min(vowels_in_middle, key=lambda x: abs(halfway - len(vowels_in_middle) // 2))
    
    return closest_vowel