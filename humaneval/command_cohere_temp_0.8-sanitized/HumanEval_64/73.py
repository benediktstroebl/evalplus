def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.
    """
    # Define the list of vowels including y at the end of the word
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    # Count the number of vowels in the string, using a list comprehension
    count = sum(1 for char in s if char in vowels)
    return count