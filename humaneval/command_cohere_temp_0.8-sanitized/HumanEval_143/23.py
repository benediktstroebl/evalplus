def is_prime(n):
    """
    Checks whether the number is prime or not.

    Args:
        n (int): Number to check if prime

    Returns:
        bool: True if n is prime, False otherwise
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

    Args:
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split(" ")
    new_words = []
    for word in words:
        if is_prime(len(word)):
            new_words.append(word)
    return " ".join(new_words)
sentence = "This is a test"