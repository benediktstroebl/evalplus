```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.filter(string)]

# Test the function with a few inputs
test_cases = [
    'abc',
    'hello world',
    'foo',
    'bar',
]

print("Test cases:")
for input, expected_result in test_cases.show(input)
print(f"Input: {input} Expected: {expected_result}")

for i, input in enumerate(test_cases):
    actual_result = all_prefixes(input)
    print(f"Test {i+1}: {input} actual: {actual_result} expected: {expected_result}")
``` 
Do you need anything else?