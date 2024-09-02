
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
    # Convert the string to a list
    s_list = list(s)

    # Reverse the list
    s_list.reverse()

    # Convert the list back to a string
    s_list_2 = ''.join(s_list)

    # Split the string into a list using spaces
    s_list_3 = s_list_2.split()

    # For each word in the list, sort it using the built-in sorted function
    # with the key parameter being the built-in ord function
    # and lambda function being used to sort each word based on the ordinal value of each character
    for i, word in enumerate(s_list_3):
        word = sorted(word, key=lambda x: ord(x))
        s_list_3[i] = ''.join(word)

    # Join the list back into a string
    s_list_4 = ''.join(s_list_3)

    return s_list_4

