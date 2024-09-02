
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # your code here

    # list of words
    words = ["name", "of", "string"]

    # convert to list of characters
    words_lst = [list(word) for word in words]

    # unique letters
    uniq_letters = []

    # each unique letter in words
    for word in words_lst:
        for letter in word:
            # if letter is not in the list of uniq letters, append it
            if letter not in uniq_letters:
                uniq_letters.append(letter)

    # count the number of unique letters in each word
    uniq_letters_count = []

    # count of each unique letter in each word
    for word in words_lst:
        count = 0
        for letter in word:
            if letter in uniq_letters:
                count += 1

        uniq_letters_count.append(count)

    # sort the count by descending order
    uniq_letters_count = sorted(uniq_letters_count, reverse=
