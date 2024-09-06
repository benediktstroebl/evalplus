def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Self-contained within the function, it defines all possible vowels:
    'a', 'e', 'i', 'o', 'u', and 'y' at the end of a word.
    """
    vowels = set('aeiou')
    if s[-1] == 'y':
        vowels.add('y')
    return sum(1 for char in s if char in vowels)