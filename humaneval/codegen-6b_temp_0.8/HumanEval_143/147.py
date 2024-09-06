
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
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    words = sentence.split()
    new_words = []
    for word in words:
        prime_word = ''
        for c in word:
            if is_prime(ord(c)):
                prime_word += c
        if prime_word != '':
            new_words.append(prime_word)

    return ' '.join(new_words)


assert words_in_sentence('This is a test') == 'is'
assert words_in_sentence('lets go for swimming') == 'go for'

