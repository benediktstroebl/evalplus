def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    It considers the vowels to be 'a', 'e', 'i', 'o', 'u', and 'y' 
    only when it is at the end of the word.
    """
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count