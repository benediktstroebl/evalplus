def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Self-contained within the function, it defines all vowels including 'y' as a special case.
    """
    vowels = set('aeiouAEIOU')
    # Define 'y' as a vowel only when it's at the end of a word (special case)
    if s[-1] == 'y' and s[-2:] == 'y':
        return len(s) // 2
    return sum(1 for char in s if char in vowels)
    # Return the count of all other vowels in the word, excluding 'y'