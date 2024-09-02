
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
    # naive solution
    # split sentence to words
    # generate prime numbers for each word in the sentence
    # put them together in an array
    # sort the array
    # return the first word from the array
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    word_list = sentence.split(' ')
    prime_list = []

    for word in word_list:
        word_length = len(word)
        word_prime = ''.join([str(x) for x in range(2, word_length + 1) if is_prime(x)])
        prime_list.append(word_prime)

    prime_list.sort()

    return prime_list[0]
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

