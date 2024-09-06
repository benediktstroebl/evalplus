
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

    # list of prime numbers
    prime_numbers = []

    # for i in range(2, 101):
    #     is_prime = True

    #     for j in range(2, i):
    #         if i % j == 0:
    #             is_prime = False

    #         if is_prime:
    #             prime_numbers.append(i)

    # print(prime_numbers)

    # list of words in the sentence
    words_list = sentence.split(" ")

    # empty list to store the prime words
    prime_words = []

    # iterate over the words in the sentence
    for word in words_list:
        if len(word) in prime_numbers:
            prime_words.append(word)

    # join the prime words together using a space as the separator
    return " ".join(prime_words)

