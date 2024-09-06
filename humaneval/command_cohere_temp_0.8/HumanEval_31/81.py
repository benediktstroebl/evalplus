```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement and test scenarios provided, accurately determining prime numbers. It begins by handling the special case of n being less than 2, ensuring that it returns False as expected. The function then progresses through a loop starting from 2 and ending at the square root of n. It checks if any integer within this range evenly divides n, and if so, it returns False, indicating that n is not prime. Lastly, if none of these conditions are met by the time the loop concludes, the function returns True, signifying that n is indeed a prime number. 

This approach allows the function to efficiently determine whether a number is prime or not, ensuring optimal performance. The code's concise structure also enhances its readability and ease of understanding, making it a reliable and maintainable solution. 

This function is crafted to effectively determine prime numbers and can be seamlessly integrated into larger projects. Feel free to adapt this code to your specific needs, and if you have further questions or requirements, don't hesitate to ask!