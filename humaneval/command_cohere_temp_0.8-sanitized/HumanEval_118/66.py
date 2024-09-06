def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word (case sensitive).
    Vowels in the beginning and ending don't count. 
    Return empty string if you didn't find any vowel met the above condition. 
    You may assume that the given string contains English letter only. 
    """
    vowels = 'AEIOUaeiou' 
    len_word = len(word)
    
    # Ensure the word has at least 2 characters to work with
    if len_word < 2: 
        return ''

    # List of all possible vowels that could potentially fit the criteria
    potential_vowels = [char for char in word if char in vowels]
    
    # Define right-most ending consonant and index, and left-most starting consonant and index
    right_conv_idx, left_conv_idx = -1, -1 
    for i, char in enumerate(word):
        if char.isalpha():
            if char.lower() in vowels:
                potential_vowels.pop(potential_vowels.index(char))
            elif potential_vowels and (right_conv_idx == -1 or i < right_conv_idx):
                right_conv_idx = i
            elif potential_vowels and (left_conv_idx == -1 or i > left_conv_idx):
                left_conv_idx = i
            
    # Special case for a single character word or all potential vowels are the start or end
    if len(potential_vowels) == 0 or (right_conv_idx == -1 and left_conv_idx == -1):
        return ''

    # Ensure there is a potential vowel between right and left consonants
    if len(potential_vowels) == 1 and right_conv_idx - left_conv_idx == 1:
        return ''

    # Return the closest vowel (if any)
    if right_conv_idx != -1 and left_conv_idx != -1:
        return potential_vowels[max(0, min(right_conv_idx, len_word - left_conv_idx) - 1)]
    else:
        return potential_vowels[0]