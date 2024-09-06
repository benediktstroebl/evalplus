
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
    def is_prime(n):
        return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

    def split_sentence(s):
        return list(filter(None, re.findall(r'\w+', s)))

    return ' '.join(filter(is_prime, map(len, split_sentence(sentence))))

