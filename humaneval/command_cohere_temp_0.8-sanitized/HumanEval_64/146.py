def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    num_vowels = 0
    word_ending = s[-1]

    if word_ending == 'a' or word_ending == 'e' or word_ending == 'i' or word_ending == 'o' or word_ending == 'u':
        num_vowels += 1

    if word_ending == 'y':
        num_vowels += 1

    return num_vowels