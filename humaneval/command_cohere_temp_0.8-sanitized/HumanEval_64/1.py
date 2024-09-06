def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.
    """
    vowel_count = 0
    words = s.split()
    for word in words:
        if len(word) > 0 and (word.endswith("ay") or word.endswith("ey") or word.endswith("iy") or word.endswith("oy") or word.endswith("uy") or word in "y"):
            vowel_count += 1
    return vowel_count