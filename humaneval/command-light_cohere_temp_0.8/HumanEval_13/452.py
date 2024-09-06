```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("both numbers must be provided")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    if not a: return b
    if not b: return a
    return max(a - b, 0)

# unit tests
test_greatest_common_divisor = []
test_data = [(3, 5), (25, 15)]
test_run = []
for a, b in test_data:
    try:
        result = greatest_common_divisor(a, b)
        test_run.append(result)
        except ValueError as e:
            test_run.append(str(e))
test_results = "\n".join(map(str, test_run))
# main function tests
print("Greatest Common Divisor:", "3", "5:", 7)
print("Greatest Common Divisor:", "25", "15:", 5)
print("Greatest Common Divisor:", "5", "13:", 3)
print("Test Results:", test_results)
```