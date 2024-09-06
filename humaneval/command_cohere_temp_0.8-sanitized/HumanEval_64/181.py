def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # Ensure that the string ending with 'y' is treated as a vowel
    if s.endswith('y') and len(s) > 1:
        s = s.replace('y','i') 
    # Using strings.count to count the number of vowels in the string
    return sum(1 for char in s if char in 'aeiou') + (s.endswith('y') and len(s) > 1)