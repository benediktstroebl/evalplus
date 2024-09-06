def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.

    Parameters:
    s (str): The input word whose vowels are to be counted.

    Returns:
    int: The number of vowels in the input word.
    """
    vowel_count = 0
    word_end = s.strip("ey")

    for char in s:
        if char in "aieou":
            vowel_count += 1
        elif char == "y" and word_end:
            vowel_count += 1

    return vowel_count