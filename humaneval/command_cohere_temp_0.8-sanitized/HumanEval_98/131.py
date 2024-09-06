def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    def has_vowels(c):
        vowels = 'AEIOUaeiou'
        return c.isupper() and c in vowels

    return sum(1 for i, char in enumerate(s, 2) if has_vowels(char) and i % 2 == 0)