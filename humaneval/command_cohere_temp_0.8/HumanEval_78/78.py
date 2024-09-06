```python
import math

def hex_key(num):
    prime_digits = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num.upper():
        if digit in prime_digits:
            count += 1
    return count
```

The algorithm consists of several steps:
1. A set called `prime_digits` is initialized that includes all primes that can be displayed in hexadecimal (`2`, `3`, `5`, `7`, `11` and `13`) to make counting of primes more efficient.
2. Then, each digit of the hexadecimal number is iterated through, and the number of digits that are present in the `prime_digits` set is counted. The sum is stored in the `count` variable.
3. Finally, this count is returned.

The script assumes that the input is always correct or empty and that the letters `A`, `B`, `C`, `D`, `E`, `F` represent their decimal equivalents.

Note: Set comprehension in Python is used to create the `prime_digits` set. Instead of putting the elements directly into the set, the set comprehension checks whether each digit is present in the `prime_digits` set. If so, the digit is added to the set and counted. Thus, the `for` loop is not necessary, making the code more concise and efficient. 

Keep in mind that in more complex problems, breaking the solution down into steps, like the algorithm provided, makes it easier to approach and ensure that each part works as expected. 

You can test the solution by calling the `hex_key()` function with different input numbers. The `set` behavior of Python automatically determines the numeric value of the letters 'A' to 'F'.