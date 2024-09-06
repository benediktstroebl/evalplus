
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

    #Return the original string if it has no spaces
    if s.find(' ') == -1:
        return s

    #Split the string into a list of words
    words = s.split()
    result = []

    #For each word in the list
    for word in words:

        #Sort the characters and join them to create new word
        result.append(''.join(sorted(word)))

    #Join the words back into a sentence
    return ' '.join(result)

