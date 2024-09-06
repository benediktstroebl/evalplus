Here's the self-contained Python function:
```python
def fizz_buzz(n: int):
    if n <= 0:
        return 0
    
    count = 0
    for i in range(2, n+1):
        digit = str(i)[0]
        if digit == '7':
            count += 1
        if count == 3:
            break
    
    return count
```
This function defines a recursive function `fizz_buzz` which aims to find out the number of times the digit 7 appears in the numbers from 2 to n. It returns the time when the count of occurrences of 7 in that range, which satisfies the problem's criteria.