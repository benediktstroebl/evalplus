
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
    split_str = s.split()
    result = ""
    for i in split_str:
        result += i
        result += " "
        for j in range(len(i)-1):
            if ord(i[j]) > ord(i[j+1]):
                i = i[:j+1] + i[j+1:j][::-1] + i[j+1:]
                j = -1
        result += i
    return result[:-1]


