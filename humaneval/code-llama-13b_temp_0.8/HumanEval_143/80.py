
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
    # def check_prime(number):
    #     for i in range(2, number):
    #         if number % i == 0:
    #             return False
    #     return True

    # s = sentence.split(' ')
    # result = ''
    # for w in s:
    #     if check_prime(len(w)):
    #         result += w + ' '
    # return result.rstrip()

    return ' '.join([w for w in sentence.split(' ') if not any(i in range(2, len(w)) for i in range(2, int(len(w) ** 0.5) + 1))])

