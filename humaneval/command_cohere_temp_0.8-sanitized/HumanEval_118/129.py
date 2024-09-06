def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    word = word.lower()
    index = next((i for i, char in enumerate(word) if char in vowels), None)
    if index == None or index == 0 or index == len(word) - 1:
        return ""
    while index < len(word) - 1:
        right_char = word[index + 1]
        if right_char in consonants:
            return word[index]
        index = next((i for i in range(index + 1, len(word)) if word[i] in vowels), None)
        if index == None or index == len(word) - 1:
            return word[index - 1]
    return ""