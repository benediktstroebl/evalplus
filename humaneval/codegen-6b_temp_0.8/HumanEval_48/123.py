

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
    # One line
    # return str(text) == str(text)[::-1]

    # String slicing
    # return text[::-1] == text

    # Deque
    # import collections
    # deque = collections.deque(text)
    # while len(deque) > 1:
    #     left = deque.popleft()
    #     right = deque.pop()
    #     if left != right:
    #         return False
    # return True

    # Two points
    # text = list(text)
    # for i in range(len(text)//2):
    #     if text[i] != text[-i-1]:
    #         return False
    # return True

    # Reversing
    # text = text.lower()
    # for i in range(len(text)//2):
    #     if text[i] != text[-i-1]:
    #         return False
    # return True

    # Palindrome is a word that reads the same forwards and backwards
    #   (even-length word)
    return text == text[::-1]
