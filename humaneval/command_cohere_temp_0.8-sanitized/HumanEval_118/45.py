def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    # Removing extra spaces and converting to lower case for case insensitivity
    word = word.strip().lower()
    index_of_right_vowel = len(word) - word[::-1].index(word[0]) - 1
    if index_of_right_vowel < 0:
        return ""
    for vowel in vowels:
        if vowel in word[index_of_right_vowel:]:
            return vowel
    return ""