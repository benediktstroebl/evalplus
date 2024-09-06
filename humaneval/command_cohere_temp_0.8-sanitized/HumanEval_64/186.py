def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowels = set('aeiou')
    word_ended_with_y = s.endswith('y')
    
    if word_ended_with_y:
        return len(vowels) + (s.count('y'))
    else:
        return s.count('y') + len(vowels)