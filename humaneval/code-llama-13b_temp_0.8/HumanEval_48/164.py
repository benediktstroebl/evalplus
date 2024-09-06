

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """

    # letters = []

    # for letter in text:
    #     letters.append(letter)

    # is_palindrome = True
    # # index = int(len(letters)/2)

    # for i in range(0, int(len(letters)/2)):
    #     if letters[i] != letters[-i-1]:
    #         is_palindrome = False
    #         break

    # return is_palindrome

    return text == text[::-1]
