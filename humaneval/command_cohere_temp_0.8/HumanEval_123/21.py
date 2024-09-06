```python
def get_odd_collatz(n):
    odd_seq = [x for x in collatz_sequence(n) if x % 2 != 0]
    return sorted(odd_seq)

def collatz_sequence(n):
    if n == 1:
        return [1]
    else:
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq
```

The `get_odd_collatz` function retrieves the odd numbers from the Collatz sequence for a given starting integer `n`. The `collatz_sequence` function calculates the entire Collatz sequence for `n`, both odd and even numbers, and the former is extracted by filtering from this sequence. The result is a list of odd numbers in the Collatz sequence, but it's not necessarily sorted. 

To sort the list, the `get_odd_collatz` function wraps the filtered sequence in a sorted function, ensuring the returned list is sorted in ascending order. This yields a sorted list of only the odd numbers from the Collatz sequence. 

The code uses the base case of the collatz sequence which is 1. Hence, the function is designed to return a list with only 1 if the input is also 1. 

This code is modular and reusable. It executes fast, thanks to Python's native list comprehension and sorting utilities. It also adheres to the problem's outlined specifications, making it an effective solution for the specified issue.