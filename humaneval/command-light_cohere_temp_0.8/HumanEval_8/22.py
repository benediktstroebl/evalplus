```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_cases = [
    [], (0, 1)
    [1, 2, 3], (6, 12)
    [10, 20, 30], (50, 300)
]

results = {}
for test_case in test_cases:
    result = sum_product(test_case)
    results[test_case] = result

for case, expected in results.
```

Let me explain the code:
-   The `sum_product` function takes a list of integers as an argument and returns a tuple with two values: the sum and the product of the integers in the list.
-   Inside uses two variables, `product` and `sum`, to calculate the product and sum of the integers, respectively.
-   The function uses a loop to iterate over each element in the list.
-   For product is initialized to 1, and then each integer in the list is multiplied with the `product` variable, and the sum of the integers is added to the `sum` variable.
-   The function then returns the tuple `(sum, product)` that contains the sum and product of the integers in the list.
-   The `test_cases` variable is a list that contains a number of test cases, each consisting of a list of integers.
-   The function then iterates over each test case in `test_cases` and calls the `sum_product` function to calculate the sum and product of the integers in the list.
-   The calculated values are stored in the `results` dictionary, with the test case as the key and the result as the value.