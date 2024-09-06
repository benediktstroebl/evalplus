def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    def check_vowels(char):
        # check if char is an uppercase vowel
        return char.isupper() and char in 'AEIOU'
    
    count = 0
    length = len(s)
    # half the length to iterate through strings with even indices only
    for i in range(length // 2):
        if check_vowels(s[i]):
            count += 1
    return count