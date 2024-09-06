def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    vowel characters are 'a', 'e', 'i', 'o', 'u', and letters 'y' 
    at the end of a word.

    Args:
        s (str): The input string to count the vowels in.

    Returns:
        int: Number of vowels in the string.
    """
    count = 0
    for char in s:
        if char in 'aieou' or (char == 'y' and s.endswith(char)): 
            count += 1
    return count