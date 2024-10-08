
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

    import re
    import math
    from functools import reduce

    def length(word):
        return len(word)
    
    def is_prime(n):
        return (n > 1) and (reduce(lambda r, x: r and (x % n!= 0), range(2, int(math.sqrt(n)) + 1), True))

    words = sentence.split(" ")
    prime_words = []
    for word in words:
        word_length = len(word)
        if is_prime(word_length):
            prime_words.append(word)
    return " ".join(prime_words)
