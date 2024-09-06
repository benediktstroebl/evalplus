def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # Define the list of vowels and integerify the string length.
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    length = len(s)

    # Count the number of vowels in the string, excluding 'y' if not at the end.
    count = sum(1 for i in range(length) if s[i] in vowels and (s[-1] != 'y' or i == length - 1))

    # Return the total count.
    return count