def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    # Define the vowels and the ending letter
    vowels = set('aeiou')
    ending_letter = 'y'

    # Initialize the count of vowels
    count = 0

    # Check each letter in the string
    for letter in s:
        if letter in vowels or (letter == ending_letter and s[-1] == ending_letter):
            count += 1

    return count