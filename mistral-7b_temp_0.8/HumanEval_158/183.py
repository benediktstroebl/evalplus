
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # step 1: put all the words in a list, and remove the duplicate words
    # step 2: for every word in the list, check if it has unique characters or not
    # step 3: return the first word in the list if the word has unique characters
    # step 4: return an empty string if there are no words with unique characters

    # words = ['aaa', 'bbb', 'cccc', 'dddddd', 'eeeeeee', 'ffffff']
    words = ['name', 'of', 'string']

    # step 1
    # put all the words in a list, and remove the duplicate words
    # words = ["name", "of", "string"]
    # words = []
    # for word in words:
    #     if word not in words:
    #         words.append(word)
    # print(words)

    # step 2
    # for every word in the list, check if it has unique characters or not
    # step 3
    # return the first word in the list if the word has unique characters
    # step 4
