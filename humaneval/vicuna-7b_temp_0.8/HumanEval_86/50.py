
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    def permute(str):
        """
        A function to permute the characters of a string.
        """
        if not str:
            return []
        else:
            result = [str]
            for i in range(1, len(str)):
                for perm in permute(str[:i]):
                    for j in range(0, len(perm), i - len(str[i])):
                        perm[j:j + i] = str[i - j - 1] + perm[j + i]
                    result.append(perm)
            return result

    return ''.join([chr(ord('a') + i) for i in range(len(s))])