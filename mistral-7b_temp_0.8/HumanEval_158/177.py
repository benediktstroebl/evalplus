
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    #makes a new list containing the list input in lower case
    words_lower = [x.lower() for x in words]
    #new list that holds the count of the unique characters
    num_of_unique_chars = []
    #new list of the unique characters
    unique_chars = []
    # loop to iterate through the list of strings
    for i in words_lower:
        #loop to iterate through each string
        for c in i:
            #if the string does not contain the character, add 1 to count of unique chars
            if c not in unique_chars:
                num_of_unique_chars.append(1)
            #if the character is already in the string, add one to count of unique chars
            else:
                num_of_unique_chars[unique_chars.index(c)] += 1
            #append the character to unique chars
            unique_chars.append(c)
    #new list of indexes of unique characters
    indexes = []
    #loop to iterate through the unique chars
    for i in unique
