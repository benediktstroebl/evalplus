
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
    # code to implement the function
    # use a queue to keep track of words as they come in
    # use a dictionary to store the characters in order
    # use a string to store the final result
    # for each word in the input string,
    # iterate over each character in the word,
    # and add it to the queue along with its ascii value
    # when a space is encountered, add the current word to the dictionary
    # and move to the next word
    # when a newline is encountered, use the dictionary to rebuild the word
    # and add it to the final string

    # TODO: Implement the above logic