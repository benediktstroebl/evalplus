```python
def factorize(n):
    factors = []
    for i in range(2,int(n**.5)+1):
        is_divisible = True
        while n%i == 0:
            n = n//i
            is_divisible = False
        if is_divisible:
            factors.append(i)
            factors.append(int(factors[-1])*i)
    return factors

# Test cases
# Test 1
print(factorize(8))
[:]
# Test 2
print(factorize(25))
[:]
# Test 3
print(factorize(70))
[:]
``` 
This function factorize takes an integer n as input and returns a list of its prime factors in descending order. It iterates through prime factors of n using a loop and checks divisibility until the square of n is reached. This process continues until the maximum factor is found and the list of prime factors is returned in descending order.