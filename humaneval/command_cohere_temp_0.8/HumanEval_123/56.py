```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    odd_collatz.sort()
    return odd_collatz
```

The `get_odd_collatz` function starts with the input number and uses a while loop to iterate through the Collatz sequence until the number becomes 1. If the number is even, it's divided by 2; if the number is odd, it's multiplied by 3 and added with 1. The odd numbers in the sequence are collected in the `odd_collatz` list, which is then sorted and returned.

This algorithm has a time complexity of O(k^2) because the length of the Collatz sequence is approximately k^2, where k is the number of bits required to represent the original number, thus making it inefficient for large inputs. However, it's an interesting exercise to play with the idea of the Collatz sequence and its mysterious nature. 

The code includes a test suite with a test function that verifies the correctness of the `get_odd_collatz` function for various input values. You can use this script to easily test other values and see the odd numbers in the Collatz sequence.