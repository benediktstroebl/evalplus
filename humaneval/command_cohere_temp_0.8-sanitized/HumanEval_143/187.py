import math
def is_prime(n):
    """
    Checks whether the number is prime or not.

    Parameters:
        n (int): Number to check if prime

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

    Parameters:
        sentence (str): The input sentence with spaces

    Returns:
        str: A new sentence with words whose lengths are prime numbers
    """
    words = sentence.split(" ")
    new_sentence = ""
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + " "
    return new_sentence