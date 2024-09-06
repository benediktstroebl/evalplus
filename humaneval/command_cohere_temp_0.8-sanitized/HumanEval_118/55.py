def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word (case sensitive).
    Vowels in the beginning and ending don't count. 
    Return empty string if you didn't find any vowel met the above condition. 
    You may assume that the given string contains English letter only. 
    """
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    
    # For the rightmost vowel excluding ending
    right_idx = len_word - 1
    for char in word:
        if char in vowels:
            right_idx = len_word - 1
            break

    # No right vowel, return empty string
    if right_idx == len_word - 1:
        return ''

    # For the leftmost vowel excluding beginning
    left_idx = 0
    for char in word:
        if char in vowels and left_idx == 0:
            left_idx = 1
            break

    # No left vowel, return the rightmost vowel
    if left_idx == 1:
        return word[right_idx]

    # Binary search for the middle vowel
    mid_idx = (right_idx + left_idx) // 2
    for i in range(mid_idx, len_word):
        if word[i] in vowels:
            mid_idx = i
            break

    # Case 1: A vowel is found between mid and right, return it
    if word[mid_idx] in vowels:
        return word[mid_idx]
    # Case 2: No vowel found between mid and right, return the right one
    else:
        return word[right_idx]