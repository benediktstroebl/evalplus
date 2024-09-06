The solution is:
```python
def fizz_buzz(n: int) -> int:
    counts = {}
    for num in range(1, n+1):
        if num % 11 == 0 or num % 13 == 0:
            digit = str(num)[1]
            if digit in counts:
                counts[digit] += 1
            else:
                counts[digit] = 1
    return max(counts.from key=counts.count, values=[7])
```
The function creates a dictionary to store the frequency of each digit and iterates over the numbers from 1 to n. It checks for the and creates the counts dictionary. The function returns the maximum count of 7 from the dictionary.