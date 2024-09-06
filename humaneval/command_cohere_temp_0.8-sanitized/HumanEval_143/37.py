import math
def is_prime(n):
    """
    Checks whether the given number is a prime number or not.

    Args:
        n (int): Number to check if it is prime

    Returns:
        bool: True if n is prime, False otherwise
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

    Args:
        sentence (str): The input sentence with spaces separating words

    Returns:
        str: A string containing words whose lengths are prime numbers
             and keeping the same order as in the input sentence
    """
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()
sentence = "This is a test"