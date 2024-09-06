
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
    # start with an empty string
    new_s = ""
    # go character by character
    for char in s:
        if char == " ":
            new_s += char
        else:
            # append the character to the end of the new string
            new_s += char
    # split the new string into a list
    new_s = new_s.split()
    # for each word in the list, sort it and join it into a new word
    for i in range(len(new_s)):
        new_s[i] = "".join(sorted(new_s[i]))
    # return the string with words sorted
    return " ".join(new_s)

