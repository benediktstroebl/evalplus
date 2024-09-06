
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
    # Use a list to keep the original sentence
    s_list = s.split(' ')
    ans = []
    for token in s_list:
        # Use a list to sort the character in a word
        temp = []
        for c in token:
            temp.append(c)
        temp.sort()
        temp = ''.join(temp)
        ans.append(temp)
    return ' '.join(ans)
