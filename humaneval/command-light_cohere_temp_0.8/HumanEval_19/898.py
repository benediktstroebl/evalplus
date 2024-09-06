```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))

# unit tests
numbers_list = ["three one five", "six three eight", "four two nine"]
test_str = "Sorted numbers should be: "
for num in numbers_list:
    test_str += f"{num} "
sorted_str = sort_numbers(" ".join(numbers_list))
test_str += ")"
print(test_str)
```