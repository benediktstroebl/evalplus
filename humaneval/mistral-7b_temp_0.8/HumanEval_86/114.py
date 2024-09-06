
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

    def make_lowercase(text):
        """
        Makes all the characters in the text to lowercase.
        """
        return text.lower()

    def split_string(text):
        """
        Splits the string based on the spaces.
        """
        return text.split(' ')

    def sort_string(text):
        """
        Sorts the text based on ASCII value.
        """
        text = sorted(list(text))
        text = ''.join(text)
        return text

    def join_text(texts):
        """
        Joins the text based on the space.
        """
        return ' '.join(texts)

    text = make_lowercase(s)
    texts = split_string(text)
    sorted_texts = []

    for text in texts:
        sorted_text = sort_string(text)
        sorted_texts.append(sorted_text)

    result = join_text(sorted_texts)
    return result
