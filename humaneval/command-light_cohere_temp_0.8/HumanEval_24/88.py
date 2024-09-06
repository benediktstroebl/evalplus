```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test cases
test_cases = [
    (0,),
    (1,),
    (2, 6),
    (3, 4),
    (4, 2, 8),
    (5, 10),
    (6, 12),
    (7, 14),
    (8, 4, 8, 14),
    (9, 9, 18),
    (10, 5, 50),
    (11, 22, 34),
    (12, 4, 36),
    (13, 10, 90),
    (14, 6, 28, 84),
    (15, 1, 45),
    (16, 4, 90, 192),
    (17, 10, 225),
    (18, 12, 324),
    (19, 20, 900),
    (20, 1, 1206),
    (21, 42, 784),
    (22, 6, 784, 2880),
    (23, 50, 3024),
    (24, 8, 84, 162880),
    (25, 100, 85664)
]

for test_case in test_cases:
    print(test_case[0], "->", largest_divisor(test_case[1]))
    print(test_case[1], "->", int())
    print(test_case[1], " largest_divisor() == ", largest_divisor(test_case[1]))
``` 
This code defines a function called largest_divisor that returns the largest number which divides the given number evenly, smaller than or equal to the given number. The code also provides a test cases to check the correctness of the largest_divisor function.