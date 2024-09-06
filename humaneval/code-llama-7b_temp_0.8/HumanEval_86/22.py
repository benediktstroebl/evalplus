
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
    # code goes here
    arr = s.split(" ")
    result = ""
    for word in arr:
        if word == "":
            result += " "
        else:
            arr1 = []
            for i in range(len(word)):
                arr1.append(word[i])
            arr1.sort()
            result += "".join(arr1) + " "
    return result[:-1]

