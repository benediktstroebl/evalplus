import re
from collections import Counter
PRIMES = Counter(filter(lambda x: len(x) > 1 and all(n % i for i in range(2, int(len(x)**0.5) + 1)),
                       set(re.split(r" \s?", input()))))
def words_in_sentence(sentence):
    return ' '.join(PRIMES[word] for word in sentence.split() if word in PRIMES)