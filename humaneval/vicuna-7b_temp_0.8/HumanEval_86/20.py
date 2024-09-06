
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
    # Sample solution
    # s = s.upper() # convert to uppercase
    # s = s.split() # split on space
    # sorted_s = sorted(s) # sort the list of words
    # for i in range(len(s)):
    #     for j in range(len(sorted_s)):
    #         if s[i] == sorted_s[j]:
    #             sorted_s[j] = sorted_s[j].upper()
    # s = ''.join(sorted_s)
    # return s

    # Alternate solution
    # s = s.upper()  # convert to uppercase
    # s = s.split()  # split on space
    # for i in range(len(s)):
    #     for j in range(len(s[i])):
    #         sorted_chars = sorted(s[i][::-1])  # sort the characters in the word
    #         s[i] = ''.join(sorted_chars)  # reassemble the sorted characters into the word
    # return s