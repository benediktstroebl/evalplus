
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
    # 1
    # words = sentence.split(" ")
    #
    # for i in range(len(words)):
    #     if isPrime(len(words[i])):
    #         print(words[i], end=" ")
    #
    # print()

    # 2
    words = []
    for i in sentence:
        if i == " ":
            if len(words) > 1 and isPrime(len(words[len(words)-1])):
                print(words.pop(), end=" ")
        else:
            words.append(i)

    if len(words) > 1 and isPrime(len(words[len(words)-1])):
        print(words.pop(), end=" ")
