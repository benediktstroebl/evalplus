Here's the answer to your prompt:
```python
def find_closest_elements(numbers: List[float]):
    closest = (numbers[0] if len(numbers) <= 2 else float('inf'))
    closest2 = float('inf')
    for n in numbers[1:]:
        if abs(numbers[0] - n) < closest2:
            closest2 = n
        elif abs(numbers[0] - n) < closest:
            closest = n
    return closest, closest2

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
best = find_closest_elements(numbers)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple with the two closest numbers in it. The function first checks if the list has at least two elements, in which case it returns the first number in the list as the closest. If the list has less than two elements, it sets the variable `closest` to the first number and `closest2` to `float('inf')`, which represents an infinite value. It then iterates over the recent elements and keeps updating the `closest` and `closest2` variables. The loop compares each element with all the remaining elements, and when it finds a smaller value than `closest2`, it updates the `closest` variable with the current element. The loop continues until all the elements have been compared, at which point the `closest` variable holds the smallest value and `closest2` holds the largest value, so the function returns the `closest` and `closest2` variables.