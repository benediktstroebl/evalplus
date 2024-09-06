
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

    # 1st solution
    # O(n) time | O(n) space
    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    words = sentence.split(" ")
    result = []
    for i in words:
        if is_prime(len(i)):
            result.append(i)
    return " ".join(result)
