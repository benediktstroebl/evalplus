def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    vowel_count = 0
    word_ending = s[-1]
    
    if word_ending == 'a' or word_ending == 'e' or word_ending == 'i' \
        or word_ending == 'o' or word_ending == 'u':
        vowel_count += 1
    if word_ending == 'y':
        vowel_count += 1
    
    # Check if the first letter of the word is a vowel
    if s[0] == 'a' or s[0] == 'e' or s[0] == 'i' \
        or s[0] == 'o' or s[0] == 'u':
        vowel_count += 1
    
    # Check if the second letter of the word is a vowel
    if len(s) > 1 and (s[1] == 'a' or s[1] == 'e' or s[1] == 'i' \
        or s[1] == 'o' or s[1] == 'u'):
        vowel_count += 1

    # Check if the third letter of the word is a vowel
    if len(s) > 2 and (s[2] == 'a' or s[2] == 'e' or s[2] == 'i' \
        or s[2] == 'o' or s[2] == 'u'):
        vowel_count += 1

    # Check the rest of the letters
    for i in range(3, len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' \
            or s[i] == 'o' or s[i] == 'u':
            vowel_count += 1

    return vowel_count