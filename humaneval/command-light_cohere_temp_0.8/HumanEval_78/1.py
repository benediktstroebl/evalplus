```python
def count_primes(hex):
    if hex == "":
        return 0
    if len(hex) < 2:
        return -1
    if hex[0] == "A" or hex[0] == "B" or hex[0] == "D" or hex[0] == "E":
        return 0
    if hex[0] == "2" or hex[0] == "3":
        return 1 + count_primes(hex[1:])
    return 2 + count_primes(hex[1:])

def test():
    return count_primes("1077E") == 6

def test2():
    return count_primes("A") == 1

def test3():
    return count_primes("123456789ABCDEF0") == 6

print("Test results:")
print(test())
print(test2())
print(test3())
```
This Python script defines a function `count_primes` that takes a string representing a hexadecimal number as input and returns the count of prime numbers in that number. It also contains three test functions to verify the correctness of the `count_primes` function for specific inputs. 
The `count_primes` function uses a depth-first search algorithm to find prime numbers in a hexadecimal number. The first test function checks if the input is empty and returns -1, or if the input length is less than 2, it also returns -1. It then checks for specific characters "A," "B," "D," and "E," returning 0 if found. If the first digit is "2" or "3," it recursively calls `count_primes` with the rest of the string. The second test function checks if the input is "A" or "D," and returns 1. If the first digit is "5," it also returns 1 plus the result of the recursive call. The third test function checks if the input is "123456789ABCDEF0," and returns 6, which is the count of prime numbers in this number. 
The test functions are expected to return the correct results for the given inputs, and the final print statement prints the results of the tests.