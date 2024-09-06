def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Convert the word to lowercase to make the comparison case insensitive
    word = word.lower()

    # Collect rightmost consonants and the vowel between them
    right_consonants = []
    right_vowel = ''
    for letter in word[1:]:
        if letter in consonants:
            right_consonants.append(letter)
        else:
            right_vowel = letter

    # Check if the rightmost consonant is the last character of the word
    if right_consonants and right_consonants[-1] == word[-1]:
        right_consonants.pop()

    if right_consonants:
        # Return the closest vowel to the right if any
        return right_vowel
    elif right_consonants == []:
        # Return the first character of the word if it's a vowel
        if word[0] in vowels:
            return word[0]
        # Otherwise, return an empty string
        else:
            return ''