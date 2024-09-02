
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
    # Split the sentence into a list of words.
    words = s.split()
    # Create a new list with the words in order.
    res = []
    # Loop through each word in the list.
    for word in words:
        # Create a new word from the current word with the characters in order.
        res.append(sorted(word))
    # Join the list of words back into a sentence.
    return " ".join(res)

