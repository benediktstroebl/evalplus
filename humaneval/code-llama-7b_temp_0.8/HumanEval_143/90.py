
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
    def is_prime(num):
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        return True

    def solution(sentence):
        res = []
        sentence = sentence.split(" ")
        for word in sentence:
            if is_prime(len(word)):
                res.append(word)
        return " ".join(res)

    return solution
