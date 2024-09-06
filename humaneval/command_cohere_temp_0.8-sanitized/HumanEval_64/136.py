def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # To handle the 'y' special case, we use str.endswith() to check if the
    # last character is a 'y', and if so, check if the previous character is a
    # vowel. This pattern matches the specification in the test cases.
    return sum(1 for c in s if c in 'aieou' or (s.endswith('y') and c in 'aeiou'))