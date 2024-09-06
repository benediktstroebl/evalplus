def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    num_vowels = 0
    word_ended_with_y = s.endswith("y")
    
    for char in s:
        if char in 'aieou':
            num_vowels += 1
        elif char == 'y' and word_ended_with_y:
            num_vowels += 1
            
    return num_vowels