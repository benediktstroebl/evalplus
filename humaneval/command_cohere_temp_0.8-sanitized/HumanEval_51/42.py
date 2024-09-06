def remove_vowels(text):
    # Create a string containing all lowercase and uppercase vowels.
    vowels = "aeiouAEIOU"
    
    # Use the translate method to remove vowels from the input text.
    # str.maketrans("", "", vowels) creates a translation table that maps
    # each character in the vowels string to None, effectively removing them.
    return text.translate(str.maketrans("", "", vowels))