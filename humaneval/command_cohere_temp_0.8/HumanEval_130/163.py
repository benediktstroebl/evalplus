```python
def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    list_of_trib = [0] * (n + 1)
    list_of_trib[0] = 1
    list_of_trib[1] = 3
    for i in range(2, n + 1):
        if i % 2 == 1:
            list_of_trib[i] = list_of_trib[i - 1] + list_of_trib[i - 2] + list_of_trib[i + 1]
        else:
            list_of_trib[i] = 1 + (i / 2)
    return list_of_trib
``` 

This Python script defines a function called `tri(n)` that calculates the first `n + 1` terms of the Tribonacci sequence. The Tribonacci sequence is an extension of the Fibonacci sequence where each term is the sum of the previous two terms, and if `n` is even, it's defined as `1 + n/2`.

The function starts by checking if `n` is 0 or 1, in which case it returns an empty list or a list with just 1 respectively, since the Tribonacci sequence starts with the number 1. Then, it initializes an array `list_of_trib` with 0es to preallocate the space needed to store the sequence, placing a 1 at index 0 and a 3 at index 1, which are the first two elements of the Tribonacci sequence.

After that, it loops through the remaining terms `2 <= i < n + 1`, calculating each element of the Tribonacci sequence according to the definition and populating the `list_of_trib` accordingly. The final result is returned as the list of the first `n + 1` numbers of the Tribonacci sequence.