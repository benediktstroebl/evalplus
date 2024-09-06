```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This script takes an input string of numbers from 'zero' to 'nine' in a space-delimited format and returns the smallest numerical value at the beginning, followed by the rest sorted in ascending order. The `split()` method isolates each number, and `map()` converts the sorted integers back to their string representation, making the output compatible with the original number format. 

Here is a usage example:
```python
print(sort_numbers('five three one'))  # one three five
```
This would output:
```one three five``` due to the sorting mechanism.