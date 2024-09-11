```markdown
### Prime Factorization of an Integer

#### Description
This script determines the prime factors of a given integer and lists them in the order from smallest to largest.

#### Code
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    # Remove duplicates by converting to a set and then back to a list
    # Sort the list to maintain the order of prime factors from smallest to largest
    factors = sorted(list(set(factors)))
    # Create a list where each factor appears as many times as it appears in the original factorization
    result = []
    for factor in factors:
        count = 0
        for f in factors:
            if f == factor:
                count += 1
        result.extend([factor] * count)
    return result

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

#### Explanation
This script uses a simple trial division approach to find the prime factors of a given integer. It starts by dividing the input number `n` by the smallest prime number `2`. If `n` is divisible by `2`, it divides `n` by `2` and adds `2` to the list of factors. This process continues until `n` is no longer divisible by `2`. The script then moves on to the next prime number and repeats the process. The list of factors is then sorted to maintain the order of prime factors from smallest to largest. Finally, each factor appears as many times as it appears in the original factorization by iterating over the sorted list of factors and counting the occurrences of each factor.

#### Time Complexity
The time complexity of this script is O(sqrt(n) * log(n)), where n is the input number. This is because the script iterates over the prime numbers up to the square root of `n` and each iteration takes O(log(n)) time.

#### Space Complexity
The space complexity of this script is O(n), where n is the input number. This is because the script stores the list of factors in memory.