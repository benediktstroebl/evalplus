
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

    list_of_prime_numbers = []
    sentence = sentence.split(' ')
    for word in sentence:
        if len(word) > 1:
            for i in range(2,len(word)):
                if word[i] == '.':
                    continue
                if int(word[i]) not in list_of_prime_numbers:
                    list_of_prime_numbers.append(int(word[i]))

    for i in list_of_prime_numbers:
        if i not in [2,3,5,7,11,13,17,19]:
            list_of_prime_numbers.remove(i)

    count = 0
    for word in sentence:
        if len(word) in list_of_prime_numbers and count < len(sentence):
            print(word)
            count += 1

