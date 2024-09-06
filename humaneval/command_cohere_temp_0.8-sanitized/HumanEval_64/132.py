def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    cnt = 0
    for c in s:
        if c in 'aieou':
            cnt += 1
        elif c == 'y' and s.endswith(c):
            cnt += 1
    return cnt