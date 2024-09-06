def is_prime(num):
    """
    Checks if a number is prime or not
    Args:
        (int) num: Number to be checked
    Returns:
        (bool) Prime or not
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
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
        (str) sentence: Input sentence

    Returns:
        (str) Words with prime lengths in the same order as the original sentence
    """
    words = sentence.split()  # Split the sentence into words using space as separator
    prime_words = [word for word in words if is_prime(len(word))]  # Filtering using generator and list comprehension

    return ' '.join(prime_words)  # Joining the prime words with space to form a string