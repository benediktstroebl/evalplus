def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'

    index = next((i for i, char in enumerate(word) if char in vowels), None)
    right_consonants = word[index:].lower()

    if index == 0 or index == len(word) - 1 or not right_consonants:
        return ""

    return vowels[right_consonants.find(consonants)]