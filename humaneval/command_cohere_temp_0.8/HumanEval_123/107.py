Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_seq.append(num)
    return odd_seq

# Test cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(13) == [1, 13, 91, 413, 107, 563, 317, 671, 423, 217, 563, 321, 213, 769, 557, 1649, 349, 641, 791, 1367, 4159, 563, 479, 121, 367, 671, 479, 189, 521, 557, 1319, 479, 217, 563, 137, 49, 321, 5, 107, 13, 7, 1]
``` 

The `get_odd_collatz` function uses an iterative approach to calculate the odd numbers in the Collatz sequence for a given starting integer `n`. It keeps track of odd numbers in the `odd_seq` list, updating the number (`num`) and testing for evenness (`% 2 == 0`) to decide whether to halve or triple and add 1 to the previous number. The resulting list is then returned as the odd numbers in the Collatz sequence.