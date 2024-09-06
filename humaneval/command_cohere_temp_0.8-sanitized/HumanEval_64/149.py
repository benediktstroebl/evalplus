def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.
    """
    # Define the list of vowels including 'y' as a vowel only at the end of a word
    vowels = ["a", "e", "i", "o", "u", "y"]
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count