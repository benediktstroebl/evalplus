def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # To count the number of vowels in a word, we iterate over each character in the word
    # and check if the character is a vowel. If the character is a vowel, we increment
    # a counter by 1. 

    # We use the 'if' and 'elif' statements to check different conditions. 
    # If a character is a vowel, we increment the counter by using the increase() method. 
    # If the character is not a vowel, the counter is unchanged. 

    counter = 0
    for char in s:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            counter += 1
        elif char == 'y' and s[-1] != 'y':
            counter += 1
    return counter