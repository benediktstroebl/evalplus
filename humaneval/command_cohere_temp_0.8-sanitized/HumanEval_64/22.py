def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # To count the number of vowels in a word, we use string concatenation
    # to add each character to a string constant boasting all vowels. If the
    # character matches a vowel, the len() of the resultant string will
    # increase.
    count = len(s + 'aeiouAEIOU')
    # If the last character of the string is 'y', and if it is the only
    # vowel in the string, we increment the count.
    if s[-1:] == 'y' and count == 1:
        return count + 1
    return count