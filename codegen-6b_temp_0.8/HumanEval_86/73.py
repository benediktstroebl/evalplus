
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
    #strip empty space
    words = s.split()
    #sort words
    x = sorted(words)
    #separate nouns from verbs
    noun_list = []
    verb_list = []
    for word in x:
        if word[0].isalpha() == True:
            noun_list.append(word)
        else:
            verb_list.append(word)
    #structure the output
    out_str = ''
    for word in verb_list:
        out_str += word[1:] + ' '
    out_str += '!'
    for word in noun_list:
        out_str += word[1:] + ' '
    return out_str.strip()

