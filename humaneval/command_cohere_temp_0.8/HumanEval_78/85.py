```python
import re

def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0
    num = re.sub('[^A-Fa-f0-9]','',num)
    if num:
        for digit in num:
            if digit in hex_digits and digit in primes:
                count += 1
    return count
```
The code uses the `re` module to remove non-hexadecimal digits and handles cases like `2020` or non-hexadecimal symbols. The primes are stored in a list for easy access and checking. 

The script solves the problem by:
- Removing all non-hexadecimal digits and symbols from the input number using regular expressions. This operation is performed by the line `num = re.sub('[^A-Fa-f0-9]','',num)`.
- Iterating over each digit in the filtered number and checking if it is a hexadecimal digit and a prime number. The prime checking is done through the list `primes` containing all the prime hexadecimal digits. This is done in the for loop `for digit in num:`.
- Incrementing the count variable if a digit satisfies both conditions. The count variable is incremented in the if statement `if digit in hex_digits and digit in primes:`.
- Returning the count variable once all digits have been checked. This is done in the line `return count`. 
To ensure the correctness of the approach, regular expressions are used to sanitize the input making sure that only hexadecimal digits are kept. PRimes are defined in the code to ensure that no external factor can change or break the program. 

Note that the code defines `primes` and `hex_digits` lists for all possible prime and hexadecimal digits. This ensures that the code is robust and can work with any valid input. However, this approach might consume more memory and time as the lists are comprehensive making the code efficient.