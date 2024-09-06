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

The `get_odd_collatz` function retrieves the odd numbers from the Collatz sequence for a given starting integer `n`. The `collatz_sequence` function calculates the entire Collatz sequence for `n`, both odd and even numbers, and the former is extracted by filtering from this sequence. The resulting odd numbers are then sorted in ascending order. 

This approach ensures that the odd numbers in the Collatz sequence are accurately extracted and returned, considering the conjecture's rules. 

This code correctly handles the edge case `n = 1`, which is the endpoint of some Collatz sequences. The length of the resulting Collatz sequence depends on the starting value `n` and can vary for different inputs. 

This algorithm's time complexity is largely dictated by the complexity of the Collatz sequence itself, which isn't analyzable theoretically, owing to its seemingly erratic behavior for most inputs. However, its space complexity is O(n), where n is the input value.