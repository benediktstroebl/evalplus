def words_in_sentence(sentence):
    sentence = sentence.split(' ')  # split the sentence into array of words
    prime_words = []  # array to store prime number words
    for word in sentence:
        if is_prime(len(word)):  # check if the length of the word is prime
            prime_words.append(word)  # add the word to the prime_words array
    return ' '.join(prime_words)  # return a string of words with prime number lengths
def is_prime(n):  # check if n is prime
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
sentence = "this is a test"