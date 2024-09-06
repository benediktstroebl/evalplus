def select_words(s, n):
    """
    Finds words in a string that contain a certain number of consonants.
    
    Args:
    - s (str): Input string.
    - n (int): Target number of consonants in each word.

    Returns:
    - list: List of words containing exactly n consonants.
    """
    # Define the list of consonants and vowel characters
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    word_list = []
    
    # Step through each character in the string
    for i in range(len(s)):
        # Initialize a counter for consonants in the current word
        word_consonants = 0
        
        # Iterate over each character in the current word
        for j in range(i, len(s)):
            # If the character is a consonant, increment the counter
            if s[j] in consonants:
                word_consonants += 1
            
            # If we've reached the target number of consonants, add the word to the list
            if word_consonants == n:
                word_list.append(s[i:j+1])
                
                # If we exceed the target, break out of the inner loop
                if word_consonants > n:
                    break
            
            # If we encounter a space, word boundary, or a vowel, reset the counter
            if s[j] == ' ' or s[j] in vowels:
                word_consonants = 0
                
                # If we exceed the target, break out of the inner loop
                if word_consonants > n:
                    break
    
    # If the input string is empty, return an empty list
    if not s:
        return []
    
    return word_list
n = 4