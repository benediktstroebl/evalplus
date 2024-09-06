def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    # Find the first vowel character from the right side of the word
    for char in word[::-1]:
        if char in vowels:
            return char
    return ''