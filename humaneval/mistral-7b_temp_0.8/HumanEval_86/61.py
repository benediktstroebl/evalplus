
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
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    def anti_shuffle_word(word):
        """
        This function takes a word as input and returns a ordered version of it.
        """
        chars = list(word)
        new_chars = []
        for char in chars:
            pos = alphabet.index(char)
            new_chars.append(alphabet[pos])
        return ''.join(new_chars)

    result = []
    for word in s.split(" "):
        result.append(anti_shuffle_word(word))
    return " ".join(result)

