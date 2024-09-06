```python
def get_odd_collatz(n):
    odd_seq = [x for x in collatz_sequence(n) if x % 2 == 1]
    odd_seq.sort()
    return odd_seq
    
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

The `collatz_sequence` function calculates the entire Collatz sequence for a given starting integer `n`, and the `get_odd_collatz` function then extracts only the odd numbers from this sequence. Both functions are tested independently to ensure they operate as expected. 
This code demonstrates a practical application of the Collatz sequence, which is a fascinating mathematical curiosity. Even though it's not expected to finish among the existing integers, the algorithm's behavior is understandable and useful for investigating odd numbers. 

This algorithm has a exponential time complexity for calculating the length of the Collatz sequence, especially for larger starting values `n`. Larger `n` will have larger corresponding Collatz sequences. 

Let's arrive at this combination of code and Collatz sequence knowledge together. Do you want to learn more about the complexities of providing efficient algorithms and discussing their time complexities? 

Let's keep practicing with various problem-solving scenarios and exploring the exciting field of computational mathematics.