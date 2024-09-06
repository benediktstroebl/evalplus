
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    #############
    # Edge Cases #
    #############
    if not sentence:
        return ""

    #############
    # Main Code #
    #############
    # use a set to keep track of words already encountered
    # initialize the set to hold the words already found
    words_found = set()
    # create the list of words to return
    words_to_return = []
    # split the sentence into a list of words
    word_list = sentence.split()
    # iterate through each word in the word list
    for word in word_list:
        # check if the word has been encountered yet
        if word not in words_found:
            # check if the length of the word is a prime number
            if is_prime(len(word)):
                # add the word to the set of words encountered
                words_found.add(word)
                # add the word to the list of words to return
                words_to_return.append(word)

    return " ".join(words_to_return)

