def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel 
    only when it's at the end of the word."""
    vowels = set('aeiou')
    word, last_char = s.lower(), s.strip()[-1:]
    return sum(c in vowels for c in word) + (last_Char in vowels if len(word)>0 else 0)