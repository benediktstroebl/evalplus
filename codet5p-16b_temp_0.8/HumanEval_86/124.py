
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

    def ascii_sort(s):
        """
        Write a function that takes a string and returns a new string where all the characters are arranged in
        ascending order based on ascii value.
        Note: You should keep the order of characters intact.

        For example:
        ascii_sort('Hi') returns 'HII'
        ascii_sort('hello') returns 'ehllo'
        ascii_sort('Hello World!!!') returns 'Hello!!!Wdlor'
        """
        s = list(s)
        l = len(s)
        for i in range(l):
            for j in range(l-1):
                if ord(s[j]) > ord(s[j+1]):
                    s[j], s[j+1] = s[j+1], s[j]
        return ''.join(s)

    words = s.split(' ')
    s = []
    for word in words:
        s.append(ascii_sort(word))
    return''.join(s)
