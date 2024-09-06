def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    def count_vowels(string):
        vowels = {'A', 'E', 'I', 'O', 'U'}
        return sum(1 for char in string if char in vowels)
    
    return sum(count_vowels(s[i]) for i in range(0, len(s), 2))