
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
    #################
    # PSEUDOCODE
    # SPLIT the sentence into words
    # CREATE a list of the prime numbers
    # CREATE a variable called index, initialize it to 0
    # LOOP through the list of words
    # if the word length is the same as the prime number at the current index, add it to a new list
    # increment the index
    # RETURN the new list

    #################
    # CLARIFYING QUESTIONS
    # DO I WANT TO RETURN A STRING OR A LIST?

    # SOLUTION 1:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    words = sentence.split(" ")
    word_list = []
    index = 0

    for word in words:
        if len(word) == primes[index]:
            word_list.append(word)
            index += 1
        if index == len(primes):
            break

    return " ".join(word_list)


    # SOLUTION 2:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    words = sentence.split(" ")
    word_list = []
    index = 0

    for word in words:
        if len(word) in primes:
            word_list.append(word)

    return " ".join(word_list)
