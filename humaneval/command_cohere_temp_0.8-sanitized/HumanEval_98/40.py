def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Using list comprehension to check if each character in the string is an uppercase vowel.
    uppercase_vowels = ['A', 'E', 'I', 'O', 'U']
    count = sum(1 for i, char in enumerate(s) if i % 2 == 0 and char in uppercase_vowels)
    return count