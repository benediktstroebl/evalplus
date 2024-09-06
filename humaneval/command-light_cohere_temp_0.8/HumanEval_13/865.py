```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0  # Handle division by zero
    return max(a, b) / gcd(a, b)

# Test cases
test_gcd = [
    (3, 5),
    (25, 15),
    # Add more test cases here...
]

test_ suite = {}
for case in test_gcd:
    assert greatest_common_divisor(case[0], case[1]) == case[2], f"Failed for {case}"

# Runtime testing using `percy.py`
 run:
import time

start_time = time.time()

def test_gcd_func():
    test_gcd_func()

end_time = time.time()

# Print the execution time
print("Execution time:", end_time - start_time, f"seconds")
```