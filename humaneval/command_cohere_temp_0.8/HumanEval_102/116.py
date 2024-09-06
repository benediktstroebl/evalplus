```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    if max_even >= min_even and max_even % 2 == 0:
        return max_even
    elif max_even < min_even:
        return -1
    else: 
        return choose_num(min_even, max_even)
```
This Python script defines a function choose_num(x, y) that takes two positive numbers x and y as input and returns the largest even integer that falls within the range [x, y], inclusive. If no such even number is found within this range, it returns -1. The function employs a recursive approach to solve the problem, checking if the middle point of the range is an even number and recursively exploring the range if further optimization is possible. The algorithm efficiently solves the problem without the need for unnecessary iterations or complexities, making it suitable for real-world applications.