
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

    def is_prime(number):
        if number <= 1:
            return False
        for x in range(2, number):
            if number % x == 0:
                return False
        return True

    def convert_to_prime(string):
        prime_list = []
        words = string.split()
        for word in words:
            if is_prime(len(word)):
                prime_list.append(word)
        return''.join(prime_list)

    return convert_to_prime(sentence)
