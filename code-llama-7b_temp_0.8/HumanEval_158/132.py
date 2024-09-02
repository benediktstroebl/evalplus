
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Your code here
    # for each word, get the length of each word
    # if there is a tie, check the lexicographical order
    # if there is still a tie, go back to the length
    # if there is still a tie, return the first word, since we have no other way to break the tie.
    # if not, return the word with the highest length
    
    longest = 0
    for word in words:
        if len(set(word)) > longest:
            longest = len(set(word))
            winner = word
    return winner
