def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.
    """
    vowels = set("aeiouy")
    ya = s.endswith("y")
    if ya:
        vowels.remove("y")
        vowels.add("i")
    return sum(1 for char in s if char in vowels)