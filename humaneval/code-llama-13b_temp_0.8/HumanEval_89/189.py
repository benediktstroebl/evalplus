
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    # Set a list of the alphabet
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # Set a list of numbers
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    # Set the length of the string
    length_s = len(s)
    # Iterate through the length of the string and set each character in a new string
    new_s = ''
    for x in range(length_s):
        # Set the character to the string
        character = s[x]
        # If the character is a letter
        if character in alphabet:
            # Find the index of the letter in the alphabet
            index_alphabet = alphabet.index(character)
            # Set a new index of the letter
            new_index_alphabet = index_alphabet + 4
            # If the new index is greater than 25
            if new_index_alphabet > 25:
                # Set the new index to 1
                new_index_alphabet = 1
            # Set the new letter to the new index in the alphabet
            new_character = alphabet[new_index_alphabet]
            # Set the new character to the new string
            new_s += new_character
        # Else if the character is a number
        elif character in numbers:
            # Find the index of the number in the numbers list
            index_numbers = numbers.index(character)
            # Set a new index of the number
            new_index_numbers = index_numbers + 4
            # If the new index is greater than 9
            if new_index_numbers > 9:
                # Set the new index to 0
                new_index_numbers = 0
            # Set the new number to the new index in the alphabet
            new_character = numbers[new_index_numbers]
            # Set the new character to the new string
            new_s += new_character
        else:
            new_s += character
    return new_s

