```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 1)

# Test cases
test_cases = [
    [],
    [1, 2, 3],
    [10, 20, 30],
    [100, 200, 300, 400]
]

results = []
for case in test_cases:
    results.append(intersperse(case, 4))

print("Test cases:", endswith("\n"))
print("--------------------"))
for result in results:
    print(f"{case} => {result}")
```