def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Extract substrings from the right half that have potential to have a vowel
    right_half = word[len(word) // 2 :]
    windows = [right_half[i: i + 2] for i in range(len(right_half) - 2)]

    # Find the vowel which is closest to the right side
    closest_idx = float('inf')
    closest_vowel = ''
    for window in windows:
        prev_idx, prev_vowel = window.find(consonants), ''
        if prev_idx != -1:
            prev_vowel = window[prev_idx]
        curr_idx, curr_vowel = window.find(vowels), ''
        if curr_idx != -1:
            curr_vowel = window[curr_idx]
        if curr_idx < prev_idx or (curr_idx == prev_idx and curr_vowel < prev_vowel):
            closest_idx, closest_vowel = curr_idx, curr_vowel
        elif prev_idx < curr_idx or (prev_idx == curr_idx and prev_vowel < curr_vowel):
            closest_idx, closest_vowel = prev_idx, prev_vowel

    # Check if the found vowel meets the criteria
    if closest_idx == float('inf'):
        return ''

    # Adjust the index and return the found vowel
    return word[len(word) - 1 - closest_idx]