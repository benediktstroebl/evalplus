def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to be checked
    :return: boolean value based on primality
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
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
    :return: sentence with words of prime length only
    """
    words = sentence.split()  # split the sentence into words using space as delimiter
    prime_words = []          # list to store prime words
    
    for word in words:
        if is_prime(len(word)):  # check if the length of the word is prime
            prime_words.append(word)   # add the word to the list if it's prime
    
    return ' '.join(prime_words)  # join prime words to form a string and return