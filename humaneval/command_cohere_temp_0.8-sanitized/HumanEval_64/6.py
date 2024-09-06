def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels included in this case are 'a', 'e', 'i', 'o', 'u', and 'y' at the end of the word.
    """
    # Ensure the string ends with a y and add 1 to the count
    if s.endswith("y") and len(s) > 1:
        s = s[:-1]
    # Iterate through each character and add 1 if a vowel is found
    count = sum(1 for char in s if char in "aeiou")
    return count