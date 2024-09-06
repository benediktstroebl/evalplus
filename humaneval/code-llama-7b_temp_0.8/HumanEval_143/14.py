
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
    # PSEUDOCODE
    #############
    # # split sentence into words
    # for each word in sentence:
    #     if word length is prime
    #         add word to list
    # return list

    # convert list to string

    # if prime_words == 0:
    #     return ''
    # else:
    #     return prime_words

    #############
    # CODE
    #############
    # prime_words = []
    # prime_word_string = ''
    # sentence_words = sentence.split(' ')
    # for word in sentence_words:
    #     if is_prime(len(word)):
    #         prime_words.append(word)
    #     prime_word_string = ' '.join(prime_words)
    # return prime_word_string

    prime_words = []
    prime_word_string = ''
    sentence_words = sentence.split(' ')
    for word in sentence_words:
        if is_prime(len(word)):
            prime_words.append(word)
            prime_word_string = ' '.join(prime_words)
    return prime_word_string
