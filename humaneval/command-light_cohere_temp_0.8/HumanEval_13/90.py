```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input must be numbers")
    return max((i) for i in range(1, max(a, b) + 1) if all(d % i == 0 for d in (a, b)))

if __name__ == "__main__":
    tests = [
        (3, 5),
        (25, 15),
        (1024, 1024),
        # Add more tests as needed
    ]

    for a, b in tests:
        print(f"Checking {a} and {b}...")
        assert greatest_common_divisor(a, b) == 1
    print("All tests passed!")
```