def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Self-contained within the function, it defines all necessary variables and operations.
    """
    # Convert string to lowercase to handle cases correctly and simplify counting
    # Using a list comprehension to remove 'y' at the end of the word and convert to lowercase
    vowels = [char for char in s if char.lower() in 'aeiou' or (char == 'y' and s[-1] != 'y')]
    
    return len(vowels)