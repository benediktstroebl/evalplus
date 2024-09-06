
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
    # [PRIME NUMBERS]
    # If a number has a prime divisor,
    # then the number is not a prime number.
    # 2 is the first prime number,
    # and all numbers divisible by 2 are not prime numbers.
    prime_numbers = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    # print(prime_numbers)

    result = []
    for word in sentence.split():
        if len(word) in prime_numbers:
            result.append(word)
    return " ".join(result)
