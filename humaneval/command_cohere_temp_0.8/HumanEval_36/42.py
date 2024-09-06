Here's a Python script that contains a function fizz_buzz(n) which solves the problem as per the test cases mentioned:
```python
def fizz_buzz(n: int):
    cnt = 0
    for i in range(1, n+1):
        if i%11==0 or i%13==0:
            cnt += str(i).count('7')
    return cnt
```
The function counts the number of times the digit '7' appears in integers less than n that are divisible by 11 or 13. The code iterates through numbers from 1 to n, and for each number, it checks if the number is divisible by 11 or 13. If true, it calculates the number of 7s in that number and adds that to the count. The final count is returned. 

This solution has a time complexity of O(n) and a space complexity of O(1) as it only performs a single pass through the integers and doesn't require any additional storage.