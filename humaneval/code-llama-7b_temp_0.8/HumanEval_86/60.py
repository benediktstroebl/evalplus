
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
    #input: string
    #output: string

    #PSEUDOCODE
    #return a new string where all words are replaced by a new word where all the
    #characters arranged in ascending order based on ascii value

    #SPLIT the string into a list of words
    #sort each word based on ascending order
    #take each word and join it back together

    s_list = s.split()

    #print(s_list)

    sorted_words = []

    for word in s_list:
        word_list = list(word)
        #print(word_list)
        word_list.sort()
        #print(word_list)
        word = ''.join(word_list)
        #print(word)
        sorted_words.append(word)

    #print(sorted_words)

    #return the new string
    return ' '.join(sorted_words)

