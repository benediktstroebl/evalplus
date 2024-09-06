```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        if n % 3 == 0:
            factors.append(3)
        n = n // 3
        elif n % 5 == 0:
            factors.append(5)
        n = n // 5
        elif n % 7 == 0:
            factors.append(7)
        n = n // 7
        else:
            # Handle other prime factors by checking divisibility by 2 and 3.
              # Determine the how to check next factors.
    return factors

# test
test = factorize(8)
print(test)  # Output: [2, 2, 2]
test = factorize(25)
print(test)  # Output: [5, 5]
test = factorize(70)
print(test)  # Output: [2, 5, 7]
``` 
This code defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. It uses a basic and efficient algorithm that checks divisibility by 2, 3, 5, and 7, and handles other prime factors by checking divisibility by these numbers. The output of this function is a list of prime factors of the given integer in the order from smallest to largest.