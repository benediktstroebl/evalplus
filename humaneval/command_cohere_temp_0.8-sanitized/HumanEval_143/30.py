def words_in_sentence(sentence):
    sentence = sentence.split(' ')
    res = []
    for word in sentence:
      if len(word) in primes:
          res.append(word)
    return ' '.join(res)
primes = [i for i in range(2, 1000) if all(i % j for j in range(3, int(i**0.5)+1, 2))]