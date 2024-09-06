
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
    # ASSUME: all the words in the sentence are lowercase
    #
    # SOLUTION:
    # 1. check if word length is prime and if it is return it
    # 2. if word is not prime, check if it contains a prime word
    # 3. if not, skip it
    #
    # ALTERNATE SOLUTION:
    # 1. create a set of prime numbers
    # 2. create a set of all words
    # 3. iterate over words
    # 4. if word length is prime, add to solution set
    # 5. if word length is not prime,
    #   a. check if it contains a prime word
    #   b. if so, add it to solution set

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_word_prime(s):
        for i in range(1, len(s)):
            if is_prime(len(s[i])):
                return True
        return False

    def is_word_prime_2(s):
        return s in s

    # Time: O(N)
    def words_in_sentence(sentence):
        s_set = set(sentence.split())
        p_set = set()

        for s in s_set:
            if is_word_prime(s):
                p_set.add(s)

        return " ".join(p_set)

    return words_in_sentence(sentence)

