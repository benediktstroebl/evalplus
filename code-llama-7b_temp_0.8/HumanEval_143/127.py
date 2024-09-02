
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
    # # Intuition:
    # * for each word in the sentence, check if the length of the word is a prime number.
    # * if the length of the word is a prime number, then add it to a list of prime number words.
    # * then return the list of prime number words separated by a space.

    # # Simple Solution:
    # prime_words = []
    # for word in sentence.split():
    #     if is_prime(len(word)):
    #         prime_words.append(word)

    # return ' '.join(prime_words)

    # # Optimized Solution:
    # prime_words = []
    # for word in sentence.split():
    #     if is_prime(len(word)):
    #         prime_words.append(word)

    # return ' '.join(prime_words)

    # # Optimized Solution:
    return ' '.join(word for word in sentence.split() if is_prime(len(word)))
