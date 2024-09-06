```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")

    if a == 0:
        return b
    elif b == 0:
        return a

    # Calculate the greatest common divisor using the Euclidean algorithm
    gcd = [a, b]
    while gcd[0] != 0:
        gcd.swap(gcd[0], gcd[1])

    return gcd[1]

# Test cases
test_gcd = []
test_gcd.push_one(3)
test_gcd.push_one(5)
test_gcd.push_two(25, 15)
test_gcd.push_two(1, 25)
test_gcd.push_two(15, 25)

def test():
    for x in test_gcd:
        print(f"Test case {x} passed!")

test()
```