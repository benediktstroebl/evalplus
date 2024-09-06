```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if any(divisible(x, n))))

def divisible(x: int, n: int) -> bool:
    return x != 0 and all(n % y == 0 for y in range(1, x))

if __name__ == "__main__":
    print(largest_divisor(15))  # Output: 5
    print(largest_divisor(27))  # Output: 27
    print(largest_divisor(9))  # Output: 9
    print(largest_divisor(21))  # Assertion Error: 21 is not a divisor of any number under 20
    ```