def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word."""
    
    # Declare vowel and consonant
    vowel = ''
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    # Split word to array by character
    word = word.lower()
    array = list(word)
    
    # Loop through the word to find if any vowel meets the problem statement
    for i in range(1, len(array)):
        if array[i] in vowels and consonants.find(array[i-1]) >= 0 and consonants.find(array[i+1]) >= 0:
            vowel = array[i]
            break

    return vowel