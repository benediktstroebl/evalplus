
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
    def is_prime(x):
        if x <= 1:
            return False
        if x == 2:
            return True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    words = sentence.split()
    result = ''
    for word in words:
        if is_prime(len(word)):
            result += word + ' '

    return result.strip()
