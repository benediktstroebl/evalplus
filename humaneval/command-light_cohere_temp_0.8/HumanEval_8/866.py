Here's a self-contained Python function that calculates and returns the sum and product of a given list of integers:
```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases for function
test_sum_product = [
    [],  # Empty list
    [1, 2, 3],  # List with sum and product generated
    [1, 2, 3, 4],  # List with sum and product calculated using other methods
]

for test_case in test_sum_product:
    print(f"Case {test_case}: {test_case[0]} * {test_case[1]} = {test_case[-1]}")
```