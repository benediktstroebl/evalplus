
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


    #Create a new string
    temp = ""

    #Loop through each word
    for word in s.split(" "):

        #Create a new list
        temp_list = []

        #Loop through each character in each word
        for char in word:
            #Add characters to list
            temp_list.append(char)

        #Sort characters and add to list
        temp_list.sort()

        #Add sorted list back to string
        temp += "".join(temp_list) + " "

    #Return final string
    return temp[:-1]
