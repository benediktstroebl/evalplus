
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
    # Write your code here
    # return None
    # TODO: This is just an example implementation, you may wish to improve it.

    if not s:
        return s

    def sort_str(s):
        return ''.join(sorted(s))

    return " ".join(sort_str(word) for word in s.split())

