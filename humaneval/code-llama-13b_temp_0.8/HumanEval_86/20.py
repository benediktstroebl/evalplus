
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

    def sort_word(word):
        """
        Sort characters in a word by ascii value
        """
        sorted_word = ''
        for char in word:
            sorted_word += ''.join(sorted(char))
        return sorted_word

    return ' '.join(sort_word(word) for word in s.split())

