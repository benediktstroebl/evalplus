def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Using list comprehension to check if each character in the string is an uppercase vowel
    uppercase_vowels = [char.upper() for char in s if char.isupper() and char in 'AEIOU']
    # Using list comprehension to check if each even index in the string contains an uppercase vowel
    even_indices = [i for i in range(0, len(s), 2) if s[i] in uppercase_vowels]
    return len(even_indices)