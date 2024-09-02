
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

assert get_odd_collatz(5) == [1, 5, 16, 8, 4, 2, 1]
assert get_odd_collatz(100) == [1, 2, 3, 5, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951209499, 5791698781, 9536712102, 13095477455, 2258514337, 36543527099, 5912867298, 87178291200, 13510783998, 23087103752, 3788120230, 61035148294, 92514785350, 14399700269, 22797920069, 35301373762, 59399691635, 89586107979, 14439657888, 25914801803, 43081818766, 71368593025, 13399837420, 26398757131, 43349443700, 7014087337, 11349031701, 183631190301, 29712150178, 480752697700, 777874204901, 1258626902501, 203650110178, 3295120949009, 579169877100, 9536712102975, 1309547745501, 2258514337000, 365435270991, 5912867298009, 8717829