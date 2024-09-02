
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
    #############
    # PSEUDOCODE
    #   - split the sentence into words
    #   - get primes for each word
    #   - filter out words whose primes > len(word)
    #   - join the words together with space
    #############

    # words = sentence.split(' ')
    # primes = [get_primes(word) for word in words]
    # words = [word for word, primes in zip(words, primes) if len(word) >= primes]

    # return ' '.join(words)

    #############
    # SOLUTION 1
    #   - create a hashmap to store primes for each word length
    #   - initialize the hashmap with primes of each word length
    #   - filter out words whose primes > len(word)
    #   - join the words together with space
    #############

    # words = sentence.split(' ')

    # primes = {}
    # for i in range(1, 100):
    #     if i == 1:
    #         continue

    #     prime = True
    #     for j in range(2, i):
    #         if i % j == 0:
    #             prime = False
    #             break

    #     if prime:
    #         primes[i] = i

    # words = [word for word in words if primes.get(len(word)) >= len(word)]
    # return ' '.join(words)

    #############
    # SOLUTION 2
    #   - create a hashmap to store primes for each word length
    #   - initialize the hashmap with primes of each word length
    #   - use a list to store the words
    #   - create a function to filter out words whose primes > len(word)
    #   - join the words together with space
    #############

    words = sentence.split(' ')
    primes = {}

    for i in range(1, 100):
        if i == 1:
            continue

        prime = True
        for
