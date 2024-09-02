
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
    # First, we will find all the prime numbers in the range of the length of the string
    # Then we will iterate over the string and check if the length of the word is a prime number.
    # If it is a prime number, we will add it to the new string.
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [x for x in range(len(sentence.split())) if is_prime(x)]

    new_str = ""
    for word in sentence.split():
        if prime_numbers.count(len(word)) > 0:
            new_str = new_str + " " + word

    return new_str[1:]
