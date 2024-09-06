
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # check if the list of words is empty
    if not words:
        return ""
    
    # initialize an empty list to store the unique characters
    unique_chars = []
    
    # iterate through the words
    for word in words:
        # check if the word is not empty
        if len(word) > 0:
            # check if the word is already in the list of unique characters
            if word in unique_chars:
                # if the word is already in the list, increment the count
                unique_chars.append(unique_chars.count(word) + 1)
            else:
                # if the word is not in the list, add it and the count as 1
                unique_chars.append(1)
    
    # sort the list of unique characters
    unique_chars = sorted(unique_chars)
    
    # check if the list of unique characters is empty or not
    if len(unique_chars) == 0:
        return ""
    else:
        # find the word with maximum number of unique characters
        word = "".join([word[i:i+1] for i in range(0, len(unique_chars), 1)])
        while word[-1] == "0":
            word = word[:-1]
        return word
