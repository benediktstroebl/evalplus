
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
    word_list = sentence.split()
    prime_list = [i for i in range(2, len(word_list) + 1) if all(n % i == 0 for n in word_list)]
    new_list = []
    for i in range(len(word_list)):
        if all(n % i == 0 for n in word_list):
            new_list.append(word_list[i])
            while len(new_list) % i == 0:
                new_list.pop()
    return ' '.join(new_list)

input_string = str(input("Enter a sentence: "))
