import math
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to check
    :return: boolean
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    :param sentence: input sentence
    :return: string containing words with prime lengths
    """
    words = sentence.split()  # split the sentence into array of words
    prime_words = []  # container for prime words
    for word in words:
        if is_prime(len(word)):  # check if the length of the word is prime
            prime_words.append(word)  # add the word to the prime words container
    return ' '.join(prime_words)  # join prime words to a string