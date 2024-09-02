
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
    prime_nums = []
    for i in range(2, len(words)):
        if is_prime_number(i):
            prime_nums.append(i)

    # print(prime_nums)
    prime_nums_words = []
    for word in words:
        if len(word) in prime_nums:
            prime_nums_words.append(word)

    prime_nums_words.sort()
    # print(prime_nums_words)

    # for word in prime_nums_words:
    #     print(word)

    # print(prime_nums_words)
    prime_nums_words = " ".join(prime_nums_words)
    return prime_nums_words

