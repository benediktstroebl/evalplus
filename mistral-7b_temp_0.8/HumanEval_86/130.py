
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
    words=[]
    final_list=[]
    #split the sentence into words
    words=s.split()
    for i in words:
        #append the characters in the word in ascending order
        final_list.append(sorted(i))
    final_string=''
    for i in final_list:
        #join the words using space
        final_string=final_string+i+' '
    return final_string[:-1]
