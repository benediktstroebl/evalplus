
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

    import math
    words = sentence.split(" ")
    output = ""
    for i in words:
        if len(i) > 1 and all([c.isdigit() for c in i]):
            prime_numbers = [j for j in range(2, int(math.sqrt(len(i))) + 1) if not any([i % j == 0 for i in range(2, int(math.sqrt(len(i))) + 1)])]
            if len(prime_numbers) == len(i):
                output += i + " "
    if len(output) > 1:
        output = output[:-1]
    return output

