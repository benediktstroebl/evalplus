```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors.

    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    def prime_factors(num: int) -> List[int]:
        i = 2
        factors = []
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        return factors

    return prime_factors(n)


# Test cases
if __name__ == "__main__":
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
```

The provided Python script defines a function `factorize` that returns the prime factors of a given integer `n`. The function uses a helper function `prime_factors` to calculate the prime factors.

Here's a step-by-step explanation of how the `prime_factors` function works:

1. Initialize a variable `i` to 2 (the smallest prime number) and an empty list `factors` to store the prime factors.

2. Start a while loop that continues until `i` squared is greater than the input number `num`.

3. Inside the loop, check if `num` is divisible by `i` by using the modulus operator (`%`). If `num` is not divisible by `i`, increment `i` by 1.

4. If `num` is divisible by `i`, divide `num` by `i` and append `i` to the `factors` list.

5. After the loop, check if `num` is greater than 1. If it is, append `num` to the `factors` list, as it is a prime factor.

6. Return the `factors` list.

The `factorize` function simply calls the `prime_factors` function with the input number `n` and returns the result.

The script includes test cases at the end to verify that the function works correctly.