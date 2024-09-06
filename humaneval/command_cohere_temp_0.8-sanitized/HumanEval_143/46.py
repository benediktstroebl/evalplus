def is_prime(n):
    """
    Checks if a number is prime
    Returns True if n is prime, False otherwise
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
    """
    words = sentence.split()  # split the sentence into words using space as delimiter
    prime_words = [word for word in words if is_prime(len(word))]  # check the length of each word
    return ' '.join(prime_words)  # join the prime words back into a string