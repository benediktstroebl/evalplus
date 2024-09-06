```python
def get_odd_collatz(n):
    odd_seq = [x for x in collatz_seq(n) if x % 2 != 0]
    return sorted(odd_seq)

def collatz_seq(n):
    if n == 1:
        return [1]
    else:
        odd_seq = collatz_seq(n//2 if n % 2 == 0 else 3*n+1)
        return odd_seq + [n] + odd_seq
```

The `get_odd_collatz` function retrieves the odd numbers from the Collatz sequence for a given starting integer `n`. The `collatz_seq` recursively constructs the sequence, yielding only odd values, which are then appended to the growing sequence. The initial value of `n` is differentiated from 1 as the edge case for the base case of the recursion, hence the special handling for `n == 1`. 

This solution's time complexity is predominantly determined by the `get_odd_collatz` function, which has a linear time complexity of O(N), where N represents the number of odd numbers in the Collatz sequence. This is because it iterates through the sequence once, and the worst-case complexity for a single traversal through the sequence is O(N). 

The auxiliary function `collatz_seq` has a time complexity of O(L), where L represents the length of the Collatz sequence. This is due to the fact that the maximum number of recursive calls is proportional to the sequence's length. However, L is inherently bounded by the magnitude of the starting integer n, and in the worst case, it grows logarithmically with N. Thus, the total time complexity of the program is dominated by the `get_odd_collatz` function, resulting in a linear time complexity of O(N).