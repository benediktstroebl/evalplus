def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    """
    num_vowels = 0
    vowels = ["a", "e", "i", "o", "u", "y"]
    word = s.lower()
    
    for char in word:
        if char in vowels:
            num_vowels += 1
    
    # Adjust the count for the special case of 'y'
    if (word[-1:] == "y" and len(word) > 1 and 
        [a for a in word[:-1] if a not in vowels]):
        num_vowels += 1
    
    return num_vowels