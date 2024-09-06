
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
    words = sentence.split(" ")
    words = [i for i in words if i != '']

    from itertools import combinations
    from math import ceil, sqrt

    limit = 10000

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(ceil(sqrt(n)))):
            if n % i == 0:
                return False
        return True

    chunks = [words[i:i + k] for k in range(1, len(words) + 1) for i in range(len(words) - k + 1)]
    acc = [sum(i) for i in chunks]

    primes = [i for i in acc if i > 1 and is_prime(i)]

    res = []
    while len(res) < len(words):
        if not primes:
            res = []
            break
        elif not res:
            res = primes[:len(primes) // 2]
        else:
            for i in primes:
                if i in res:
                    continue
                else:
                    possible_words = [item for item in chunks if item[0] == i]
                    if len(possible_words) == 1:
                        res.append(i)
                        primes.remove(i)
                    else:
                        for item in possible_words:
                            if item in res:
                                continue
                            else:
                                chunk = item
                                chunk_word = item[0]
                                chunk_word_count = [item for item in chunks if item[0] == chunk_word][0]
                                if chunk_word_count[-1] in res:
                                    continue
                                else:
                                    res.append(chunk_word_count[-1])
                                    primes.remove(chunk_word)
                                    break
    return " ".join([i for i in res])
