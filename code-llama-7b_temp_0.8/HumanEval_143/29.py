
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
    # O(N) time | O(N) space - where N is the length of the input sentence
    # since we're looping through the input sentence once
    def words_in_sentence(sentence):
        words = sentence.split()
        primes = []
        for word in words:
            is_prime = True
            if len(word) == 1:
                primes.append(word)
            else:
                for num in range(2, len(word)):
                    if len(word) % num == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(word)
        return " ".join(primes)
