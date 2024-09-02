
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
    # O(26 * n) time | O(n) space
    def has_prime_length(string):
        if len(string) == 1 and string != '1':
            return True
        for i in range(2, int(len(string) ** 0.5)+1):
            if len(string) % i == 0 and is_prime(i):
                return True
        return False

    def is_prime(n):
        i = 2
        while i * i <= n:
            if n % i != 0:
                i += 1
            else:
                return False
        return True

    words = sentence.split(' ')
    return ' '.join([word for word in words if has_prime_length(word)])
