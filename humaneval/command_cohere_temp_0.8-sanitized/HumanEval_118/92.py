def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end of a word don't count.
    Empty string is returned if no qualifying vowel is found.
    """
    # We'll be using English lowercase vowels as constants
    vowels = 'aeiou'
    
    # Using right slice to extract a substring from the right of the word (excluding end)
    right_slice = word[1:-1]
    
    # Using find to check if any vowel exists in the right_slice
    vowel_index = right_slice.find(vowels)
    
    # If a vowel is found, we return the corresponding character from the original word
    if vowel_index != -1:
        return word[vowel_index+1]
    
    # If no right vowels are found, we return an empty string
    return ''